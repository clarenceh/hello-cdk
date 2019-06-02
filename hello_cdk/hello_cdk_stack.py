from aws_cdk import (
    cdk,
    aws_s3 as s3
)

class HelloCdkStack(cdk.Stack):

    def __init__(self, app: cdk.App, id: str, **kwargs) -> None:
        super().__init__(app, id)

        # S3 bucket for this stack
        bucket = s3.Bucket(self, 
            "MyFirstBucket", 
            bucket_name="my-cdk-bucket",
            versioned=True,
            encryption=s3.BucketEncryption.KmsManaged,)
