import time
import boto3
starting_time=time.time()
dynamodb=boto3.resource("dynamodb")
table=dynamodb.Table("student")
output=table.scan()
rows=output["Items"]
while "LastEvaluatedKey" in output:
    output=table.scan(ExclusiveStartKey=output["LastEvaluatedKey"])
    rows.extend(output["Items"])
time_taken=(time.time()-starting_time)*1000
print("Time for Table Read: %s" % time_taken + " ms")