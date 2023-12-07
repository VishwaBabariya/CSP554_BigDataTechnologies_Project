import pymongo
import sys
import csv
import time

client = pymongo.MongoClient('mongodb://sampath2001:gtaViceCity@docdb-2023-11-18-14-16-26.cgsuxumkpxi6.us-east-1.docdb.amazonaws.com:27017/?tls=true&tlsCAFile=global-bundle.pem&retryWrites=false')
db = client['mydatabase3']
collection = db['mycollection']
collection = db['students']

def insert_csv_to_db(csv_file):
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            student_data = {
                'FirstName': row['First Name'],
                'LastName': row['Last Name'],
                'Age': int(row['Age']),
                'Gender': row['Gender'],
                'TotalGrades': float(row['Total Grades'])
            }
            collection.insert_one(student_data)
            
            
def create_student(student_data):
    collection.insert_one(student_data)

def create_students(students_data):
    collection.insert_many(students_data)
    
def read_students(query):
    return list(collection.find(query))
    
def update_students(query, update):
    collection.update_many(query, {'$set': update})
    
def update_students_bulk(queries_updates):
    for query, update in queries_updates:
        collection.update_many(query, {'$set': update})


def delete_students(query):
    collection.delete_many(query)
    
def delete_students_bulk(queries):
    for query in queries:
        collection.delete_many(query)



            


csv_file = 'final.csv'  # Update with the path to your CSV file
insert_csv_to_db(csv_file)


#calculating time for single insertion
start_time = time.time()
create_student({
    'ID': '12345',
    'FirstName': 'John',
    'LastName': 'Doe',
    'Age': 20,
    'Gender': 'Male',
    'TotalGrades': 265.5
})
end_time = time.time()
print(f"Time taken for single insertion is: {(end_time - start_time) * 1000} milliseconds")
print()

#calculating time for multiple insertion
start_time = time.time()
create_students([
    {'ID': '67890', 'FirstName': 'Alice', 'LastName': 'Smith', 'Age': 21, 'Gender': 'Female', 'TotalGrades': 280.0},
    {'ID': '54321', 'FirstName': 'Bob', 'LastName': 'Johnson', 'Age': 22, 'Gender': 'Male', 'TotalGrades': 290.0}
])
end_time = time.time()
print(f"Time taken for multiple insertion is: {(end_time - start_time) * 1000} milliseconds")
print()
#calculating the time for single read operartion
start_time = time.time()
students_in_city = read_students({'City': 'New York'})
end_time = time.time()
print(f"Time taken for single read operation is: {(end_time - start_time) * 1000} milliseconds")
print()
#calculating the time for multiple read operation
start_time = time.time()
students_in_city = read_students({'City': 'New York'})
end_time = time.time()
print(f"Time taken for multiple read operation is: {(end_time - start_time) * 1000} milliseconds")
print()
#calculating time for single update operation
start_time = time.time()
update_students({'ID': '12345'}, {'TotalGrades': 275.0})
end_time = time.time()
print(f"Time taken for single update operation is: {(end_time - start_time) * 1000} milliseconds")
print()
#calculating time for multiple update operation
start_time = time.time()
update_students_bulk([
    ({'ID': '12345'}, {'Age': 21}),
    ({'ID': '67890'}, {'Age': 22})
])
end_time = time.time()
print(f"Time taken for multiple update operation is: {(end_time - start_time) * 1000} milliseconds")
print()
#calcultating time for single delete operation
start_time = time.time()
delete_students({'ID': '67890'})
end_time = time.time()
print(f"Time taken for single delete operation is: {(end_time - start_time) * 1000} milliseconds")
print()
#calculating time for multiple delete operation
start_time = time.time()
delete_students_bulk([
    {'ID': '12345'},
    {'ID': '67890'}
])
end_time = time.time()
print(f"Time taken for multiple delete operation is: {(end_time - start_time) * 1000} milliseconds")
print()
