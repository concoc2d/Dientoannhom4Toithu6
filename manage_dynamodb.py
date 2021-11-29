from client_factory import DynamoDBClient
from dynamodb import DynamoDB
import json
import boto3
import index

def get_dynamodb():
    dynamodb_client = DynamoDBClient().get_client()
    dynamodb = DynamoDB(dynamodb_client)
    return dynamodb

def create_dynamodb_table():
    dynamodb_client = DynamoDBClient().get_client()
    dynamodb = DynamoDB(dynamodb_client)

    table_name = "studentpy"

    # define attributes
    attribute_definitions = [
        {
            'AttributeName': 'studentid',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'lastName',
            'AttributeType': 'S'
        },
    ]

    # key schema definitions
    key_schema = [
        {
            'AttributeName': 'studentid',
            'KeyType': 'HASH'  # Partition key
        },
        {
            'AttributeName': 'lastName',
            'KeyType': 'RANGE'  # Sort key
        }
    ]

    ProvisionedThroughput = {
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }

    dynamodb_create_table_response = dynamodb.create_table(table_name, attribute_definitions, key_schema, ProvisionedThroughput)
    print("Created DynamoDB Table named " + table_name + ":" + str(dynamodb_create_table_response))


def describe_table():
    print(str(get_dynamodb().describe_table("Movies")))


def update_table_iops():
    get_dynamodb().update_read_write_capacity("s3", "Nguyen3","contact","address")


def delete_table(self):
    get_dynamodb().delete_table_with_name(self)
def delete_item(d1,d2):
    get_dynamodb().delete_item(d1,d2)
def get_item(g1,g2):
    res=get_dynamodb().get_item(g1,g2)

    print(res['Item'])
    return res['Item']
def put_item(s1,s2,s3,s4,s5,s6,s7):
    get_dynamodb().put_item(s1,s2,s3,s4,s5,s6,s7)
def up_item(u1,u2,u3,u4,u5,u6,u7):
    get_dynamodb().update_item(u1,u2,u3,u4,u5,u6,u7)
def list_table():
    res = get_dynamodb().list_table()
    print(res['Items'])
    return res['Items']

def load_table():
    with open("src/moviedata.json") as json_file:
        movie_list = json.load(json_file)
    get_dynamodb().load_movies("studentpy",movie_list)
if __name__ == '__main__':
    # create_dynamodb_table()
    # describe_table()
    # update_table_iops()
    # delete_table()
    # up_table()
    # up_item()
    # load_table()
    # delete_item()
    # get_item()
    # put_item()
    list_table()