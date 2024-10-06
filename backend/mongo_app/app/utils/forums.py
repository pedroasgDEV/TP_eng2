from bson.objectid import ObjectId
from app.utils.connectDB import MongoDB
from app.config import mongodb_config

class Forums:
    def __init__(self, mongo: MongoDB, subject_code):
        self.__database = mongo.get_database()
        self.__collection = self.__database[subject_code]
        
    # CREATE
    def insert(self, doc):
        try:
            # Insert document
            result = self.__collection.insert_one(doc)
            return {"status": "success", "_id": str(result.inserted_id)}
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    # READ
    def select(self, pipeline):
        try:
            # Execute the aggregation
            result = list(self.__collection.aggregate(pipeline))
            for doc in result:
                doc["_id"] = str(doc["_id"])
            return {"status": "success", "result": result}
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    # UPDATE
    def update(self, id, doc):
        try:
            obj_id = ObjectId(id)
            # Update document
            result = self.__collection.update_one(
                {"_id": obj_id},
                {"$set": doc}
            )
            
            return {"status": "success", "modified_count": result.modified_count}
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    # DELETE
    def delete(self, filter):
        try:
            result = self.__collection.delete_many(filter)
            return {"status": "success", "deleted_count": result.deleted_count}
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    # DELETE - entire collection
    def delete_collection(self):
        try:
            self.__collection.drop()
            self.__collection = None
            return {"status": "success", "message": "Collection dropped successfully."}
        except Exception as e:
            return {"status": "error", "message": str(e)}