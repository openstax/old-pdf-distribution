import boto3
import json

# import requests


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    ddb_client = boto3.client('dynamodb')

    response = ddb_client.get_item(
        TableName='kevin-sam-hello-world-ConfigVersionTable-1QZDCSVDY1ASO',
        Key={'current': {'S': 'current'}},
    )

    cur_config_id = response['Item']['data']['S']

    response = ddb_client.get_item(
        TableName='kevin-sam-hello-world-ConfigsTable-O8A9K3QHQBP5',
        Key={'config_id': {'S': cur_config_id}},
    )

    return {
        'statusCode': 200,
        'body': json.dumps(response['Item'])
    }
    # return {
    #     "statusCode": 200,
    #     "body": json.dumps({
    #         "message": "new hello world",
    #         # "location": ip.text.replace("\n", "")
    #     }),
    # }
