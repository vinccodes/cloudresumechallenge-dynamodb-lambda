import boto3
from botocore.exceptions import ClientError

# Create Table 
def create_visitor_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    # create the table
    table = dynamodb.create_table(
        TableName='Visitors',
        KeySchema = [
            {
                'AttributeName': 'property',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'property',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    # Wait until Table exists
    table.wait_until_exists()

    print(table.table_status)

    return table


def delete_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Visitors')
    table.delete()
    return {"message": "deleted table"}

""" 
Add table item with "count" and "visitor_total" attributes.
"""
def initialize_count(property,dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
    
    table = dynamodb.Table('Visitors')
    response = table.put_item(
        Item={
            'property': property,
            'visitor_total': 0
        }
    )

    return response


""" 
Update item with "count" and "visitor_total" attributes.
"""
def update_count(key,dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Visitors')

    response = table.update_item(
        Key={
            'property': key
        },
        UpdateExpression="set visitor_total = visitor_total + :val" ,
        ExpressionAttributeValues={
            ':val': 1,
        },
        ReturnValues="UPDATED_NEW"
    )
    return response


def get_count(key, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Visitors')

    try:
        response = table.get_item(Key={'property': key})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']


def delete_count(key, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Visitors')

    try:
        response = table.delete_item(
            Key={
                'property': key,
            }
        )
    except ClientError as e:
        if e.response['Error']['Code'] == "ConditionalCheckFailedException":
            print(e.response['Error']['Message'])
        else:
            raise
    else:
        return response

