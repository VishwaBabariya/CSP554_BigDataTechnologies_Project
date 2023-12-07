import time
import boto3
starting_time=time.time()
dynamodb=boto3.resource("dynamodb")
table=dynamodb.Table("student")
table.put_item(
   Item={
        "ID":"21",
        "First Name":"Ashley",
        "Last Name":"Walker",
        "Gender":"Female",
        "City":"Tucson",
        "State":"Arizona" 
    }
)
time_taken=(time.time()-starting_time)*1000
print("Time for Single Insertion: %s" % time_taken + " ms")
