#calculating time for single insertion
start_time = time.time()
create_grade({
    'ID': '12345',
    'Age': 20,
    'Grade1': 88.5,
    'Grade2': 92.0,
    'Grade3': 85.0,
    'TotalGrades': 265.5
})
end_time = time.time()
print(f"Time taken for single insertion is: {(end_time - start_time) * 1000} milliseconds")
print()

#calculating time for multiple insertion
start_time = time.time()
create_grades([
    {'ID': '12345', 'Age': 20, 'Grade1': 88.5, 'Grade2': 92.0, 'Grade3': 85.0, 'TotalGrades': 265.5},
    {'ID': '67890', 'Age': 21, 'Grade1': 78.5, 'Grade2': 88.0, 'Grade3': 90.0, 'TotalGrades': 256.5}
])
end_time = time.time()
print(f"Time taken for multiple insertion is: {(end_time - start_time) * 1000} milliseconds")
print()
#calculating the time for single read operartion
start_time = time.time()
grades_of_student = read_grades({'ID': '12345'})
end_time = time.time()
print(f"Time taken for single read operation is: {(end_time - start_time) * 1000} milliseconds")
print()
#calculating the time for multiple read operation
start_time = time.time()
grades_of_student = read_grades({'ID': '12345'})
end_time = time.time()
print(f"Time taken for multiple read operation is: {(end_time - start_time) * 1000} milliseconds")
print()
#calculating time for single update operation
start_time = time.time()
update_grades({'ID': '12345'}, {'TotalGrades': 270.0})
end_time = time.time()
print(f"Time taken for single update operation is: {(end_time - start_time) * 1000} milliseconds")
print()
#calculating time for multiple update operation
start_time = time.time()
update_grades_bulk([
    ({'ID': '12345'}, {'TotalGrades': 270.0}),
    ({'ID': '67890'}, {'TotalGrades': 260.0})
])
end_time = time.time()
print(f"Time taken for multiple update operation is: {(end_time - start_time) * 1000} milliseconds")
print()
#calcultating time for single delete operation
start_time = time.time()
delete_grades({'ID': '12345'})
end_time = time.time()
print(f"Time taken for single delete operation is: {(end_time - start_time) * 1000} milliseconds")
print()
#calculating time for multiple delete operation
start_time = time.time()
delete_grades_bulk([
    {'ID': '12345'},
    {'ID': '67890'}
])
end_time = time.time()
print(f"Time taken for multiple delete operation is: {(end_time - start_time) * 1000} milliseconds")
print()
