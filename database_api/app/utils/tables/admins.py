from app.utils.connectDB import PostgreSQL
from app.models.admin import Admin

class Admins:
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
        
    #insert data from a json
    def insert(self, doc):
        sql = f'''
            INSERT INTO admins 
            (name, email, passwrd, derp)
            VALUES 
            ('{doc["name"]}', '{doc["email"]}', '{doc["passwrd"]}', '{doc["derp"]}');
        '''
        
        return self.__postgre.execute(sql)
    
    #select by id
    def select(self, id):
        sql = f'''
            SELECT * FROM admins
            WHERE id = {id};
        '''
        
        result = self.__postgre.consult(sql)
        if result is not None:
            adm = Admin(result[0][0], result[0][1], result[0][2],
                       result[0][3], result[0][4])
            return adm

        else: return result
        
    #select all
    def select_all(self):
        sql = f'''
            SELECT * FROM admins;
        '''
        
        results = self.__postgre.consult(sql)
        adms = []
        
        if results is not None:
            for result in results:
                adm = Admin(result[0], result[1], result[2],
                       result[3], result[4])
                
                adms.append(adm)
                
            return adms

        else: return result

    #select by derp
    def select_derp(self, derp):
        sql = f'''
            SELECT * FROM admins WHERE derp = '{derp}';
        '''
        
        results = self.__postgre.consult(sql)
        adms = []
        
        if results is not None:
            for result in results:
                adm = Admin(result[0], result[1], result[2],
                       result[3], result[4])
                
                adms.append(adm)
                
            return adms

        else: return result
    
    #update data
    def update(self, id, doc):
        upd = ""
        for index in doc:
            upd += f"{index} = '{doc[index]}', "
            
        upd = upd[:-2]
        
        sql = f'''
            UPDATE admins
            SET {upd}
            WHERE id = '{id}';
        '''
        
        return self.__postgre.execute(sql)
    
    #delet data
    def delete(self, id):
        sql = f'''
            DELETE FROM admins
            WHERE id = '{id}';
        '''
        
        return self.__postgre.execute(sql)