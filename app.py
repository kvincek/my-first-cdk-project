#!/usr/bin/env python3

from aws_cdk import core
import os
from my_first_cdk_project.my_first_cdk_project_stack import MyFirstCdkProjectStack
# from resource_stacks.custom_vpc import CustomVpcStack
# from resource_stacks.custom_ec2 import CustomEc2Stack
app = core.App()

# CustomVpcStack(app, "my-custom-vpc-stack",  env={'account': os.environ['CDK_DEFAULT_ACCOUNT'], 
#                                                  'region': os.environ['CDK_DEFAULT_REGION']
#   })


# env_US = core.Environment(account=app.node.try_get_context('prod')['account'],
#                           region=app.node.try_get_context('prod')['region']
#                           )
#S3
MyFirstCdkProjectStack(app, "my-first-cdk-project")
# print(app.node.try_get_context('prod')['region'])
#VPC
# CustomVpcStack(app, "my-custom-vpc-stack")



app.synth()
