from app.test.dbCRUD import CRUDtest
import time

crudTest = CRUDtest()

doc = {
    "User": "21.1.4015",
    "Type": "POST",
    "text": "MENSSAGE",
    "time": time.time()
}

if crudTest.test_insert(doc): print("   . CREATE operation works :)")
else: print("   . CREATE operation is't work :(")

pipeline = [
    {"$match": { "User": "21.1.4015" }},
    {"$sort": {"time": -1}}
]

if crudTest.test_select(pipeline): print("   . READ operation works :)")
else: print("   . READ operation is't work :(")

doc = {
    "text": "NEW MENSSAGE"
}

if crudTest.test_update(doc): print("   . UPDATE operation works :)")
else: print("   . UPDATE operation is't work :(")

filter = { "User": "21.1.4015" }

if crudTest.test_delete(filter): print("   . DELETE operation works :)")
else: print("   . DELETE operation is't work :(")

if crudTest.test_delete_collection(): print("   . DELETE COLLECTION operation works :)")
else: print("   . DELETE COLLECTION operation is't work :(")