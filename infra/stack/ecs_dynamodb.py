from aws_cdk import (
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns,
    aws_dynamodb as dynamodb
    core,
)


class AutoScalingFargateService(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, *kwargs)

        # Create a cluster
        vpc = ec2.Vpc(self, "Vpc", max_azs=1)

        cluster = ecs.Cluster(self, 'fargate-service-autoscaling', vpc=vpc)

        # Create Fargate Service with container
        fargate_service = ecs_patterns.NetworkLoadBalancedFargateService(
            self,
            "sample-app",
            cluster=cluster,
            task_image_options={
                'image':
                ecs.ContainerImage.from_registry("amazon/amazon-ecs-sample")
            })

        fargate_service.service.connections.security_groups[
            0].add_ingress_rule(peer=ec2.Peer.ipv4(vpc.vpc_cidr_block),
                                connection=ec2.Port.tcp(80),
                                description="Allow http inbound from VPC")

        # Setup AutoScaling policy
        scaling = fargate_service.service.auto_scale_task_count(max_capacity=2)
        scaling.scale_on_cpu_utilization(
            "CpuScaling",
            target_utilization_percent=50,
            scale_in_cooldown=core.Duration.seconds(60),
            scale_out_cooldown=core.Duration.seconds(60),
        )

        core.CfnOutput(
            self,
            "LoadBalancerDNS",
            value=fargate_service.load_balancer.load_balancer_dns_name)

        

        # create dynamo table
        demo_table = dynamodb.Table(
            self, "devops_challenge",
            partition_key=dynamodb.Attribute(
                name="id",
                type=dynamodb.AttributeType.STRING
            )
        )     

        # grant container read/write permission to example table
        demo_table.grant_read_data(producer_lambda)
        demo_table.grant_write_data(producer_lambda)

