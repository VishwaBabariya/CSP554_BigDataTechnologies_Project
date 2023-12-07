import time
import boto3
starting_time=time.time()
dynamodb=boto3.resource("dynamodb")
table=dynamodb.Table("final")
table.update_item(
    Key={
        "ID":"21",
    },
    UpdateExpression="SET #attribute1=:value1,Age=:value2",
    ExpressionAttributeNames={
        "#attribute1":"First Name"
    },
    ExpressionAttributeValues={
        ":value1":"Ashlyn",
        ":value2":"19"
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
