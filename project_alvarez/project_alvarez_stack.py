from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)

from constructs import Construct


class ProjectAlvarezStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        my_lambda = _lambda.Function(self, 'HelloHandler',
                                     runtime=_lambda.Runtime.PYTHON_3_8,
                                     code=_lambda.Code.from_asset(
                                         'project_alvarez/lambda'),
                                     handler='hello.handler')

        apigw.LambdaRestApi(self, 'Endpoint',
                            handler=my_lambda)
