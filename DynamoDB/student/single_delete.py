import time
import boto3
starting_time=time.time()
dynamodb=boto3.resource("dynamodb")
table=dynamodb.Table("student")
table.delete_item(
    Key={
       "ID":"3"
    }
)
print("Row with ID=3 has been deleted.")
time_taken=(time.time()-starting_time)*1000
print("Time for Single Deletion: %s" % time_taken + " ms")