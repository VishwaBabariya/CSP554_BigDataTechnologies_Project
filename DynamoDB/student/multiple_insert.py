import time
import boto3
starting_time=time.time()
dynamodb=boto3.resource("dynamodb")
table=dynamodb.Table("student")
with table.batch_writer() as batch:
    batch.put_item(
        Item={
            "ID":"22",
            "First Name":"Daniel",
            "Last Name":"Kim",
            "Gender":"Male",
            "City":"Burns",
            "State":"Oregon"  
        }
    )
    batch.put_item(
        Item={
            "ID":"23",
            "First Name":"Will",
            "Last Name":"Smith",
            "Gender":"Male",
            "City":"Burlington",
            "State":"Vermont" 
        }
    )
time_taken=(time.time()-starting_time)*1000
print("Time for Multiple Insertions: %s" % time_taken + " ms")
