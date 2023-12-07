from pymongo import MongoClient
from bson import ObjectId
import time

def insertSingle():
    uri = "mongodb+srv://user1:userpass1@cluster00.exyhaaw.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    db_collection = client['SunithDB']['grades']
    start_time = time.time()
    data={'Age':18,'Grade 1':100,'Grade 2':100,'Grade 3':100,'Total Grades':300}
    db_collection.insert_one(data)
    end_time = time.time()
    print(f"{data} inserted successfully, The time time taken for Single insertion is {end_time-start_time} seconds")
    client.close()


def insertMultiple():
    uri = "mongodb+srv://user1:userpass1@cluster00.exyhaaw.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    db_collection = client['SunithDB']['grades']
    start_time = time.time()
    data=[{'Age':17,'Grade 1':96,'Grade 2':68,'Grade 3':97,'Total Grades':291},{'Age':18,'Grade 1':97,'Grade 2':99,'Grade 3':98,'Total Grades':294}]
    db_collection.insert_many(data)
    end_time = time.time()
    print(f"{data} inserted successfully, The time time taken for Multiple insertion is {end_time-start_time} seconds")
    client.close()


def updateSingle():
    uri = "mongodb+srv://user1:userpass1@cluster00.exyhaaw.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    db_collection = client['SunithDB']['grades']
    start_time = time.time()
    identifier = {'_id': ObjectId('65704821872ab6c3f92ed41b')}
    update = {'$set':{'Age':19}}
    db_collection.update_one(identifier,update)
    end_time = time.time()
    print(f"{update} Updated Successfully, The time time taken for Single Updation is {end_time-start_time} seconds")
    client.close()  


def updateMultiple():
    uri = "mongodb+srv://user1:userpass1@cluster00.exyhaaw.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    db_collection = client['SunithDB']['grades']
    start_time = time.time()
    identifier1 = {'_id': ObjectId('657048eee938e51bf19679ed')}
    identifier2 = {'_id': ObjectId('657048eee938e51bf19679ee')}
    update1 = {'$set':{'Age':18}}
    update2 = {'$set':{'Age':17}}
    db_collection.update_one(identifier1,update1)
    db_collection.update_one(identifier2,update2)
    end_time = time.time()
    print(f"{update1,update2} Updated Successfully, The time time taken for Multiple Updation is {end_time-start_time} seconds")
    client.close()  

def findSingle():
    uri = "mongodb+srv://user1:userpass1@cluster00.exyhaaw.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    db_collection = client['SunithDB']['grades']
    start_time = time.time()
    identifier = {'_id': ObjectId('65704821872ab6c3f92ed41b')}
    output=db_collection.find_one(identifier)
    end_time = time.time()
    print(f"{output} Found Successfully, The time taken for Single Reading is {end_time-start_time} seconds")


def findMultiple():
    uri = "mongodb+srv://user1:userpass1@cluster00.exyhaaw.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    db_collection = client['SunithDB']['grades']
    start_time = time.time()
    output=db_collection.find()
    for document in output:
        print(document)
    end_time = time.time()
    print(f"All the contents Read Successfully, The time taken for Multiple Read is {end_time-start_time} seconds")


def deleteSingle():
    uri = "mongodb+srv://user1:userpass1@cluster00.exyhaaw.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    db_collection = client['SunithDB']['grades']
    start_time = time.time()
    content = {'_id':ObjectId('65703cb5de104a2c39e3b65f')}
    db_collection.delete_one({'_id':ObjectId('65703cb5de104a2c39e3b65f')})
    end_time = time.time()
    print(f"{content} Document deleted successfully, The time taken for Single deletion is {end_time-start_time} seconds")
    client.close()


def deleteMultiple():
    uri = "mongodb+srv://user1:userpass1@cluster00.exyhaaw.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    db_collection = client['SunithDB']['grades']
    start_time = time.time()
    contents = {'_id': {'$in': [ObjectId('657048eee938e51bf19679ed'), ObjectId('657048eee938e51bf19679ee')]}}
    db_collection.delete_many(contents)
    end_time = time.time()
    print(f"{contents} documents deleted successfully, The time taken for multiple deletion is {end_time-start_time} seconds")
    client.close()
