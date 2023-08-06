'''
Database object model
'''

import pymongo

# TO DO: Designed for local server, needs to be hosted on cloud

class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['VMS']

    # insert one document into db
    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert_one(data)
    
    # delete one document from db
    @staticmethod
    def delete(collection, data):
        Database.DATABASE[collection].delete_one(data)

    # finds all
    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    # finds one
    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)