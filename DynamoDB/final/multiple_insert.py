import time
import boto3
starting_time=time.time()
dynamodb=boto3.resource("dynamodb")
table=dynamodb.Table("final")
with table.batch_writer() as batch:
    batch.put_item(
        Item={
            "ID":"22",
            "First Name":"Daniel",
            "Last Name":"Kim",
            "Age":"17",
            "Gender":"Male",
            "Total Grades":"291"  
        }
    )
    batch.put_item(
        Item={
            "ID":"23",
            "First Name":"Will",
            "Last Name":"Smith",
            "Age":"18",
            "Gender":"Male",
            "Total Grades":"294"  
        }
    )
time_taken=(time.time()-starting_time)*1000
print("Time for Multiple Insertions: %s" % time_taken + " ms")
