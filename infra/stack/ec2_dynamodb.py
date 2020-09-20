import aws_cdk.core as core
import aws_cdk.aws_iam as iam
import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_s3 as s3
import aws_cdk.aws_dynamodb as dynamodb


class EC2DynamoDBStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Network configuration
        subnet1 = ec2.SubnetConfiguration(
            name="Public",
            subnet_type=ec2.SubnetType.PUBLIC,
        )

        vpc = ec2.Vpc(
            self,
            "TheVPC",
            cidr="10.0.0.0/16",
            enable_dns_hostnames=True,
            enable_dns_support=True,
            max_azs=2,
            subnet_configuration=[subnet1],
        )

        # This will export the VPC's ID in CloudFormation under the key
        # 'vpcid'
        core.CfnOutput(self, "vpcid", value=vpc.vpc_id)

        # AMI
        amzn_linux = ec2.MachineImage.latest_amazon_linux(
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            edition=ec2.AmazonLinuxEdition.STANDARD,
            virtualization=ec2.AmazonLinuxVirt.HVM,
            storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE)

        # Instance Role and SSM Managed Policy
        role = iam.Role(
            self,
            "InstanceSSM",
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
        )

        role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name(
                "service-role/AmazonEC2RoleforSSM"))

        userdata_file = open("./userdata.sh", "rb").read()

        # Creates a userdata object for Linux hosts
        userdata = ec2.UserData.for_linux()

        # Adds one or more commands to the userdata object.
        userdata.add_commands(str(userdata_file, 'utf-8'))
        
        # Creates a file in the instance using s3 content
        # This is not a good solution for production. Just here for completeness.
        bucket = s3.Bucket.from_bucket_name(self, 'TheSecretsBucket','demo-secrets')
        bucket.grant_read(role, "*")
        initfile = ec2.InitFile.from_s3_object('/app/.env', bucket, '.env')

        # Instance
        instance = ec2.Instance(
            self,
            "Instance",
            instance_type=ec2.InstanceType("t3.nano"),
            machine_image=amzn_linux,
            vpc=vpc,
            role=role,
            user_data=userdata,
            init=ec2.CloudFormationInit.from_elements(initfile)       
        )

        # create dynamo table
        demo_table = dynamodb.Table(
            self,
            'TheTable',
            table_name="devops_challenge",
            partition_key=dynamodb.Attribute(
                name="code_name",
                type=dynamodb.AttributeType.STRING,
            ),
        )

        role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                resources=[demo_table.table_arn],
                actions=["dynamodb:GetItem"],
            ))
      