import time
import boto3
starting_time=time.time()
dynamodb=boto3.resource("dynamodb")
table=dynamodb.Table("student")
table.update_item(
    Key={
        "ID":"21",
    },
    UpdateExpression="SET #attribute1=:value1",
    ExpressionAttributeNames={
        "#attribute1":"First Name"
    },
    ExpressionAttributeValues={
        ":value1":"Ashlyn"
    }
)
output=table.get_item(
    Key={
        "ID":"21",
    }
)
row=output["Item"]
print(row)
time_taken=(time.time()-starting_time)*1000
print("Time for Single Update: %s" % time_taken + " ms")
