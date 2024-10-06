from app.utils.connectDB import MongoDB
from app.utils.forums import Forums
from app.config import mongodb_config

class CRUDtest:
    def __init__(self):
        #Start connection
        mongo = MongoDB(mongodb_config["HOST"], mongodb_config["PORT"], mongodb_config["DATABASE"])

        print("___________________ Database CRUD test ___________________")
        
        self.__forum = Forums(mongo, "BCC263")
        self.__id = None
    
    def test_insert(self, doc):
        doc_insert = self.__forum.insert(doc)

        if doc_insert["status"] == "success": 
            self.__id = doc_insert["inserted_id"]
            return True
        else: return False
    
    def test_select(self, pipeline):
        docs_read = self.__forum.select(pipeline)
        
        if docs_read["status"] == "success": return True
        else: return False
        
    def test_update(self, doc):
        doc_update = self.__forum.update(self.__id, doc)
        
        if doc_update["status"] == "success": return True
        else: return False
        
    def test_delete(self, filter):
        doc_del = self.__forum.delete(filter)

        if doc_del["status"] == "success": return True
        else: return False
    
    def test_delete_collection(self):
        col_del = self.__forum.delete_collection()
        
        if col_del["status"] == "success": return True
        else: return False
    