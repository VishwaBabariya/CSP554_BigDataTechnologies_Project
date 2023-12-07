import time
import boto3
starting_time=time.time()
dynamodb=boto3.resource("dynamodb")
table=dynamodb.Table("final")
table.put_item(
   Item={
        "ID":"21",
        "First Name":"Ashley",
        "Last Name":"Walker",
        "Age":"18",
        "Gender":"Female",
        "Total Grades":"300" 
    }
)
time_taken=(time.time()-starting_time)*1000
print("Time for Single Insertion: %s" % time_taken + " ms")
