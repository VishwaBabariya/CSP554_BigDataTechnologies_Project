import time
import boto3
starting_time=time.time()
dynamodb=boto3.resource("dynamodb")
table=dynamodb.Table("grades")
with table.batch_writer() as batch:
    batch.put_item(
        Item={
            "ID":"22",
            "Age":"17",
            "Grade 1":"96",
            "Grade 2":"98",
            "Grade 3":"97",
            "Total Grades":"291"  
        }
    )
    batch.put_item(
        Item={
            "ID":"23",
            "Age":"18",
            "Grade 1":"97",
            "Grade 2":"99",
            "Grade 3":"98",
            "Total Grades":"294"  
        }
    )
time_taken=(time.time()-starting_time)*1000
print("Time for Multiple Insertions: %s" % time_taken + " ms")
