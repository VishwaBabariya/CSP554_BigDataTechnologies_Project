import time
import boto3
starting_time=time.time()
dynamodb=boto3.resource("dynamodb")
table=dynamodb.Table("final")
output=table.get_item(
    Key={
        "ID":"21",
    }
)
time_taken=(time.time()-starting_time)*1000
print("Time for Single Read: %s" % time_taken + " ms")