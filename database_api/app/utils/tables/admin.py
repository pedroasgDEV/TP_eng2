from app.utils.connectDB import PostgreSQL
from app.models.admin import Admin as obj_admin

class Admin:
    def __init__(self):
        #connect the database 
        self.__postgre = PostgreSQL()
        
        if not self.__table_check(): raise Exception("ERRO: Table not exists")

    
    #check if the table exists
    def __table_check(self):
        
        sql = '''  
            SELECT * 
            FROM information_schema.tables 
            WHERE table_schema = 'public' 
            AND table_name = 'admins';
        '''
        
        result = self.__postgre.consult(sql)
        
        if result is None or len(result) != 1: return False
        else: return True