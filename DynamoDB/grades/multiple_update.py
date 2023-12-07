import time
import boto3
starting_time=time.time()
dynamodb=boto3.resource("dynamodb")
table=dynamodb.Table("grades")
table.update_item(
    Key={
        "ID":"22",
    },
    UpdateExpression="SET Age=:value1",
    ExpressionAttributeValues={
        ":value1":"18"
    }
)
table.update_item(
    Key={
        "ID":"23",
    },
    UpdateExpression="SET Age=:value1",
    ExpressionAttributeValues={
        ":value1":"17"
    }
)
output1=table.get_item(
    Key={
        "ID":"22",
    }
)
output2=table.get_item(
    Key={
        "ID":"23",
    }
)
row1=output1["Item"]
print(row1)
row2=output2["Item"]
print(row2)
time_taken=(time.time()-starting_time)*1000
print("Time for Multiple Updates: %s" % time_taken + " ms")
