import time
import boto3
starting_time=time.time()
dynamodb=boto3.resource("dynamodb")
table=dynamodb.Table("grades")
table.update_item(
    Key={
        "ID":"21",
    },
    UpdateExpression="SET Age=:value1",
    ExpressionAttributeValues={
        ":value1":"19"
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
