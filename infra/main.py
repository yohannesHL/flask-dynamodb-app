from aws_cdk import core
from stack.ec2_dynamodb import EC2DynamoDBStack

app = core.App()
EC2DynamoDBStack(app, "aws-ec2-dynamodb")
app.synth()
