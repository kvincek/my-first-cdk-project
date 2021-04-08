from aws_cdk import (
    aws_s3 as _s3,
    aws_iam as _iam,
    aws_kms as _kms,
    core
)

class MyFirstCdkProjectStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, is_prod=False, ** kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        _s3.Bucket(
            self,
            "yitongfirstcdkproject",
            versioned=False,
            encryption=_s3.BucketEncryption.S3_MANAGED,
            # encryption_key=mykey,
            block_public_access=_s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy=core.RemovalPolicy.RETAIN
        )


