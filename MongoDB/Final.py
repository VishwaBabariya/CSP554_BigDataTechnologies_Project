from pymongo import MongoClient
import time
from bson import ObjectId

def insertSingle():
    uri = "mongodb+srv://user1:userpass1@cluster00.exyhaaw.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    db_collection = client['SunithDB']['final']
    start_time = time.time()
    data={'First Name':'Ashley','Last Name':'Walker','Age':18,'Gender':'Female','Total Grades':300}
    db_collection.insert_one(data)
    end_time = time.time()
    print(f"{data} inserted successfully, The time time taken for Single insertion is {end_time-start_time} seconds")
    client.close()

def insertMultiple():
    uri = "mongodb+srv://user1:userpass1@cluster00.exyhaaw.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    db_collection = client['SunithDB']['final']
    start_time = time.time()
    data=[{'First Name':'Daniel','Last Name':'Kim','Age':17,'Gender':'Male','Total Grades':291},{'First Name':'Will','Last Name':'Smith','Age':18,'Gender':'Male','Total Grades':294}]
    db_collection.insert_many(data)
    end_time = time.time()
    print(f"{data} inserted successfully, The time time taken for Single insertion is {end_time-start_time} seconds")
    client.close()


def updateSingle():
    uri = "mongodb+srv://user1:userpass1@cluster00.exyhaaw.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    db_collection = client['SunithDB']['final']
    start_time = time.time()
    identifier = {'_id': ObjectId('657048729550c8617f5de26c')}
    update = {'$set':{'First Name':'Ashlyn','Age':19}}
    db_collection.update_many(identifier,update)
    end_time = time.time()
    print(f"{update} Updated Successfully, The time time taken for Single Updation is {end_time-start_time} seconds")
    client.close() 


def updateMultiple():
    uri = "mongodb+srv://user1:userpass1@cluster00.exyhaaw.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    db_collection = client['SunithDB']['final']
    start_time = time.time()
    identifier1 = {'_id': ObjectId('657048b51845950ce948a006')}
    identifier2 = {'_id': ObjectId('657048b51845950ce948a007')}
    update1 = {'$set':{'First Name':'Danny','Age':18}}
    update2 = {'$set':{'Last Name':'Smithson','Age':17}}
    db_collection.update_one(identifier1,update1)
    db_collection.update_one(identifier2,update2)
    end_time = time.time()
    print(f"{update1,update2} Updated Successfully, The time time taken for Multiple Updation is {end_time-start_time} seconds")
    client.close() 

def findSingle():
    uri = "mongodb+srv://user1:userpass1@cluster00.exyhaaw.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    db_collection = client['SunithDB']['final']
    start_time = time.time()
    identifier = {'_id': ObjectId('657048729550c8617f5de26c')}
    output=db_collection.find_one(identifier)
    end_time = time.time()
    print(f"{output} Found Successfully, The time time taken for Single Reading is {end_time-start_time} seconds")

def findMultiple():
    uri = "mongodb+srv://user1:userpass1@cluster00.exyhaaw.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    db_collection = client['SunithDB']['final']
    start_time = time.time()
    output=db_collection.find()
    for document in output:
        print(document)
    end_time = time.time()
    print(f"All the contents Read Successfully, The time taken for Multiple Read is {end_time-start_time} seconds")


def deleteSingle():
    uri = "mongodb+srv://user1:userpass1@cluster00.exyhaaw.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    db_collection = client['SunithDB']['final']
    start_time = time.time()
    content = {'_id':ObjectId('65703c96de104a2c39e3b64a')}
    db_collection.delete_one({'_id':ObjectId('65703c96de104a2c39e3b64a')})
    end_time = time.time()
    print(f"{content} Document deleted successfully, The time taken for Single deletion is {end_time-start_time} seconds")
    client.close()

def deleteMultiple():
    uri = "mongodb+srv://user1:userpass1@cluster00.exyhaaw.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    db_collection = client['SunithDB']['final']
    start_time = time.time()
    contents = {'_id': {'$in': [ObjectId('657048b51845950ce948a006'), ObjectId('657048b51845950ce948a007')]}}
    db_collection.delete_many(contents)
    end_time = time.time()
    print(f"{contents} documents deleted successfully, The time taken for multiple deletion is {end_time-start_time} seconds")
    client.close()