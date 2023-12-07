import time
import boto3
starting_time=time.time()
dynamodb=boto3.resource("dynamodb")
table=dynamodb.Table("grades")
table.put_item(
   Item={
        "ID":"21",
        "Age":"18",
        "Grade 1":"100",
        "Grade 2":"100",
        "Grade 3":"100",
        "Total Grades":"300" 
    }
)
time_taken=(time.time()-starting_time)*1000
print("Time for Single Insertion: %s" % time_taken + " ms")
