from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

class MongoDB:
    def __init__(self, host, port, database):
        self.__link = f"mongodb://{host}:{port}/"
        self.__client = None
        self.__database = None
        
        try:
            self.__connectDB(database)
        except ConnectionFailure as e: print(e)
        
    def __connectDB(self, database):
        try:
            self.__client = MongoClient(self.__link)
            self.__database = self.__client[database]
        except ConnectionFailure as e:
            raise ConnectionFailure(f"Failed to connect to MongoDB: {e}")
    
    def get_client(self):
        return self.__client
    
    def get_database(self):
        return self.__database
