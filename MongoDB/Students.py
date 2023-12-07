from pymongo import MongoClient
import time
from bson import ObjectId

def insertSingle():
    uri = "mongodb+srv://user1:userpass1@cluster00.exyhaaw.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    db_collection = client['SunithDB']['student']
    start_time = time.time()
    data={'First Name':'Ashley','Last Name':'Walker','Gender':'Female','City':'Tucson','State':'Arizona'}
    db_collection.insert_one(data)
    end_time = time.time()
    print(f"{data} inserted successfully, The time time taken for Single insertion is {end_time-start_time} seconds")
    client.close()


def insertMultiple():
    uri = "mongodb+srv://user1:userpass1@cluster00.exyhaaw.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    db_collection = client['SunithDB']['student']
    start_time = time.time()
    data=[{'First Name':'Daniel','Last Name':'Kim','Gender':'Male','City':'Burns','State':'Oregon'},{'First Name':'Will','Last Name':'Smith','Gender':'Male','City':'Burlington','State':'Vermont'}]
    db_collection.insert_many(data)
    end_time = time.time()
    print(f"{data} inserted successfully, The time time taken for Multiple insertion is {end_time-start_time} seconds")
    client.close()

def updateSingle():
    uri = "mongodb+srv://user1:userpass1@cluster00.exyhaaw.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    db_collection = client['SunithDB']['student']
    start_time = time.time()
    identifier = {'_id': ObjectId('6570477ac051ce8e94c97e81')}
    update = {'$set':{'First Name':'Ashlyn'}}
    db_collection.update_one(identifier,update)
    end_time = time.time()
    print(f"{update} Updated Successfully, The time time taken for Single Updation is {end_time-start_time} seconds")
    client.close() 


def updateMultiple():
    uri = "mongodb+srv://user1:userpass1@cluster00.exyhaaw.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    db_collection = client['SunithDB']['student']
    start_time = time.time()
    identifier1 = {'_id': ObjectId('6570494eefbd4cfaf10e847b')}
    identifier2 = {'_id': ObjectId('6570494eefbd4cfaf10e847c')}
    update1 = {'$set':{'First Name':'Danny'}}
    update2 = {'$set':{'Last Name':'Smithson'}}
    db_collection.update_one(identifier1,update1)
    db_collection.update_one(identifier2,update2)
    end_time = time.time()
    print(f"{update1,update2} Updated Successfully, The time time taken for Multiple Updation is {end_time-start_time} seconds")
    client.close()  

def findSingle():
    uri = "mongodb+srv://user1:userpass1@cluster00.exyhaaw.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    db_collection = client['SunithDB']['student']
    start_time = time.time()
    identifier = {'_id': ObjectId('6570477ac051ce8e94c97e81')}
    output=db_collection.find_one(identifier)
    end_time = time.time()
    print(f"{output} Found Successfully, The time taken for Single Reading is {end_time-start_time} seconds")


def findMultiple():
    uri = "mongodb+srv://user1:userpass1@cluster00.exyhaaw.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    db_collection = client['SunithDB']['student']
    start_time = time.time()
    output=db_collection.find()
    for document in output:
        print(document)
    end_time = time.time()
    print(f"All the contents Read Successfully, The time taken for Multiple Read is {end_time-start_time} seconds")


def deleteSingle():
    uri = "mongodb+srv://user1:userpass1@cluster00.exyhaaw.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    db_collection = client['SunithDB']['student']
    start_time = time.time()
    db_collection.delete_one({'_id':ObjectId('65703cbdde104a2c39e3b674')})
    end_time = time.time()
    print(f"Document deleted successfully, The time taken for Single deletion is {end_time-start_time} seconds")
    client.close()

def deleteMultiple():
    uri = "mongodb+srv://user1:userpass1@cluster00.exyhaaw.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    db_collection = client['SunithDB']['student']
    start_time = time.time()
    contents = {'_id': {'$in': [ObjectId('6570494eefbd4cfaf10e847b'), ObjectId('6570494eefbd4cfaf10e847c')]}}
    db_collection.delete_many(contents)
    end_time = time.time()
    print(f"{contents} documents deleted successfully, The time taken for multiple deletion is {end_time-start_time} seconds")
    client.close()
