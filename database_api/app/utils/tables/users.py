from app.utils.connectDB import PostgreSQL
from app.models.user import User

class Users:
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
            AND table_name = 'users';
        '''
        
        result = self.__postgre.consult(sql)
        
        if result is None or len(result) != 1: return False
        else: return True
        
    #insert data from a json
    def insert(self, doc):  
        sql = f'''
            INSERT INTO users 
            (regis_id, name, email, passwrd, course)
            VALUES 
            ('{doc["regis_id"]}', '{doc["name"]}', '{doc["email"]}', '{doc["passwrd"]}', '{doc["course"]}');
        '''
        
        return self.__postgre.execute(sql)
    
    #select by regis_id
    def select(self, regis_id):
        sql = f'''
            SELECT * FROM users
            WHERE regis_id = '{regis_id}';
        '''
        
        result = self.__postgre.consult(sql)
        if result is not None:
            usr = User(result[0][0], result[0][1], result[0][2],
                       result[0][3], result[0][4])
            return usr

        else: return result
    
    #update data
    def update(self, regis_id, doc):
        upd = ""
        for index in doc:
            upd += f"{index} = '{doc[index]}', "
            
        upd = upd[:-2]
        
        sql = f'''
            UPDATE users
            SET {upd}
            WHERE regis_id = '{regis_id}';
        '''
        
        return self.__postgre.execute(sql)
    
    #delet data
    def delete(self, regis_id):
        sql = f'''
            DELETE FROM users
            WHERE regis_id = '{regis_id}';
        '''
        
        return self.__postgre.execute(sql)