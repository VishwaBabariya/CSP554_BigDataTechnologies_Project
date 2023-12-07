import time
import boto3
starting_time=time.time()
dynamodb=boto3.resource("dynamodb")
table=dynamodb.Table("student")
table.update_item(
    Key={
        "ID":"22",
    },
    UpdateExpression="SET #attribute1=:value1",
    ExpressionAttributeNames={
        "#attribute1":"First Name"
    },
    ExpressionAttributeValues={
        ":value1":"Danny"
    }
)
table.update_item(
    Key={
        "ID":"23",
    },
    UpdateExpression="SET #attribute1=:value1",
    ExpressionAttributeNames={
        "#attribute1":"Last Name"
    },
    ExpressionAttributeValues={
        ":value1":"Smithson"
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
