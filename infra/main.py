from aws_cdk import core
from ecs_autoscaling import AutoScalingFargateService

app = core.App()
AutoScalingFargateService(app, "aws-ecs-dynamodb-autoscaling")
app.synth()