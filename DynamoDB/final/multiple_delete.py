import time
import boto3
starting_time=time.time()
dynamodb=boto3.resource("dynamodb")
table=dynamodb.Table("final")
table.delete_item(
    Key={
       "ID":"22"
    }
)
table.delete_item(
    Key={
       "ID":"23"
    }
)
print("Rows with ID=22 and ID=23 has been deleted.")
time_taken=(time.time()-starting_time)*1000
print("Time for Multiple Deletion: %s" % time_taken + " ms")