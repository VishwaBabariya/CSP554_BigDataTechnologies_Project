import pymongo
import sys
import csv
import time

client = pymongo.MongoClient('mongodb://sampath2001:gtaViceCity@docdb-2023-11-18-14-16-26.cgsuxumkpxi6.us-east-1.docdb.amazonaws.com:27017/?tls=true&tlsCAFile=global-bundle.pem&retryWrites=false')
db = client['mydatabase1']
collection = db['mycollection']
collection = db['students']

# Function to read CSV and insert into MongoDB
def insert_csv_to_db(csv_file):
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Ensure the keys match the CSV column headers
            student_data = {
                'FirstName': row['First Name'],
                'LastName': row['Last Name'],
                'Gender': row['Gender'],
                'City': row['City'],
                'State': row['State']
            }
            # Insert the data into the MongoDB collection
            collection.insert_one(student_data)

# CRUD Operations
def create_student(student_data):
    collection.insert_one(student_data)
    
def create_students(students_data):
    collection.insert_many(students_data)

def read_student(query):
    return collection.find_one(query)
    
def read_students(query):
    return list(collection.find(query))

def update_student(query, update):
    collection.update_one(query, {'$set': update})
    
def update_students(query, update):
    collection.update_many(query, {'$set': update})

def delete_student(query):
    collection.delete_one(query)
    
def delete_students(query):
    collection.delete_many(query)

# Example Usage
csv_file = 'student.csv'  # Update with the path to your CSV file
#Inserting the csv file to the databases
insert_csv_to_db(csv_file)
#calculating time for single insertion
start_time = time.time()
create_student({'FirstName': 'John', 'LastName': 'Doe', 'Gender': 'Male', 'City': 'New York', 'State': 'NY'})
end_time = time.time()
print(f"Time taken for single insertion is: {(end_time - start_time) * 1000} milliseconds")
print()

#calculating time for multiple insertion
start_time = time.time()
create_students([
    {'FirstName': 'Alice', 'LastName': 'Smith', 'Gender': 'Female', 'City': 'Boston', 'State': 'MA'},
    {'FirstName': 'Bob', 'LastName': 'Johnson', 'Gender': 'Male', 'City': 'Denver', 'State': 'CO'},
    {'FirstName': 'Carol', 'LastName': 'Davis', 'Gender': 'Female', 'City': 'Seattle', 'State': 'WA'},
    {'FirstName': 'David', 'LastName': 'Martinez', 'Gender': 'Male', 'City': 'Miami', 'State': 'FL'}
])
end_time = time.time()
print(f"Time taken for multiple insertion is: {(end_time - start_time) * 1000} milliseconds")
print()
#calculating the time for single read operartion
start_time = time.time()
read_student({'FirstName': 'John', 'LastName': 'Doe'})
end_time = time.time()
print(f"Time taken for single read operation is: {(end_time - start_time) * 1000} milliseconds")
print()
#calculating the time for multiple read operation
start_time = time.time()
students_in_city = read_students({'City': 'Boston'})
end_time = time.time()
print(f"Time taken for multiple read operation is: {(end_time - start_time) * 1000} milliseconds")
print()
#calculating time for single update operation
start_time = time.time()
update_student({'FirstName': 'John', 'LastName': 'Doe'}, {'City': 'Los Angeles', 'State': 'CA'})
end_time = time.time()
print(f"Time taken for single update operation is: {(end_time - start_time) * 1000} milliseconds")
print()
#calculating time for multiple update operation
start_time = time.time()
update_students({'City': 'Boston'}, {'State': 'MA - Updated'})
end_time = time.time()
print(f"Time taken for multiple update operation is: {(end_time - start_time) * 1000} milliseconds")
print()
#calcultating time for single delete operation
start_time = time.time()
delete_student({'FirstName': 'John', 'LastName': 'Doe'})
end_time = time.time()
print(f"Time taken for single delete operation is: {(end_time - start_time) * 1000} milliseconds")
print()
#calculating time for multiple delete operation
start_time = time.time()
delete_students({'City': 'Boston'})
end_time = time.time()
print(f"Time taken for multiple delete operation is: {(end_time - start_time) * 1000} milliseconds")
print()
