import boto3
from boto3.dynamodb.conditions import Key,Attr
class DynamoDB:
    def __init__(self, client):
        self._client = client
        """ :type : pyboto3.dynamodb """

    def create_table(self, table, attribute_definitions, key_schema, iops):
        print("Creating DynamoDB table...")
        return self._client.create_table(
            TableName=table,
            AttributeDefinitions=attribute_definitions,
            KeySchema=key_schema,
            ProvisionedThroughput=iops
        )

    def describe_table(self, table):
        print("Describing DynamoDB table with name " + table)
        return self._client.describe_table(TableName=table)

    def update_read_write_capacity(self, table_name, id, name, contact, address):
        print("Updating Provisioned Throughput of table with name " + table_name)
        return self._client.update_table(
            TableName=table_name,
            AttributeDefinitions={
                'student': id,
                'lastName': name,
                'info': {
                    'address': address,
                    'contact':contact
                }
            }
        )

    def update_movie(self,lastName, studentid, address, contact, dynamodb=None):

        response = self._client.describe_table(TableName="studentpy")
        # return response.update_item(
        #     Key={
        #         'studentid': studentid,
        #         'lastName': lastName
        #     },
        #     UpdateExpression="set info.rating=:r, info.plot=:p",
        #     ExpressionAttributeValues={
        #         ':r': address,
        #         ':p': contact
        #
        #     },
        #     ReturnValues="UPDATED_NEW"
        # )
        print(response)

    def load_movies(self,movies, dynamodb=None):
        for movie in movies:
            studentid = int(movie['studentid'])
            lastName = movie['lastName']
            print("Adding movie:", studentid, lastName)
            self.put_item(Item=movie)
    def put_movie(self,lastName, studentid,address , contact, dynamodb=None):
        self._client.put_item(
            Item={
                'studentid': studentid,
                'lastName': lastName,
                'info': {
                    'address': {"S" :address},
                    'contact': {"S" :contact}
                }
            }
        )
    def update_item(self,studentid,lastName,email,contact,address,classsv,faculty):
        return self._client.update_item(
            TableName="studentpy",
            Key={
                'studentid':{'S':studentid},
                'lastName':{'S':lastName}
            },
            UpdateExpression='SET #email=:email,#contact=:contact,#address=:address ,#classsv=:classsv,#faculty=:faculty',
            ExpressionAttributeNames={
                '#email': 'email',
                '#contact': 'contact',
                '#address':'address',
                '#classsv':'classsv',
                '#faculty':'faculty'
            },
            ExpressionAttributeValues={
                ':email':{'S':email},
                ':contact':{'S':contact},
                ':address': {'S': address},
                ':classsv': {'S': classsv},
                ':faculty': {'S': faculty}
            },
            ReturnValues="UPDATED_NEW"
        )
    def list_table(self):
        return self._client.scan(
            TableName="studentpy"
        )
    def delete_item(self,studentid,lastName):
        Key={
            'studentid':{'S':studentid},
            'lastName':{'S':lastName}
        }
        return self._client.delete_item(
            TableName="studentpy",
            Key=Key
        )
    def get_item(self,studentid,lastName):
        Key={
            'studentid':{'S':studentid},
            'lastName':{'S':lastName}
        }
        res= self._client.get_item(
            TableName="studentpy",
            Key=Key
        )
        return res
    def put_item(self,studentid,lastName,email,contact,ngaysinh,address,classsv,faculty):
        Item={
            'studentid': {'S': studentid},
            'lastName': {'S': lastName},
            'email': {'S': email},
            'contact': {'S': contact},
            'ngaysinh': {'S': ngaysinh},
            'address': {'S': address},
            'classsv': {'S': classsv},
            'faculty': {'S': faculty}
        }
        return self._client.put_item(
            TableName="studentpy",
            Item=Item
        )
    def delete_table_with_name(self, table_name):
        print("Deleting DynamoDB table with name " + table_name)
        return self._client.delete_table(TableName=table_name)