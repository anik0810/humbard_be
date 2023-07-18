from pymongo import MongoClient

try:
    client = MongoClient("")
    database = client['e_litmus']
    print('connection successfugit initlly')
except:
    print('connection fail')
