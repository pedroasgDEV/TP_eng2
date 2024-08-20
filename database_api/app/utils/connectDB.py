import psycopg2
from app.config import postgresql_config

class PostgreSQL:
    def __init__(self):
        self.__conn = psycopg2.connect(
            host = postgresql_config["HOST"],
            database = postgresql_config["DATABASE"],
            user = postgresql_config["USERNAME"],
            password = postgresql_config["PASSWORD"],
            port = postgresql_config["PORT"] 
        )
        
    @property
    def database(self):
        return self.__conn
    
    def execute(self, sql):
        try:
            cursor = self.__conn.cursor()
            cursor.execute(sql)
            cursor.close()
            self.__conn.commit()
            
        except:
            return False
        
        return True

    def consult(self, sql):
        resp = None
        
        try:
            cursor = self.__conn.cursor()
            cursor.execute(sql)
            resp = cursor.fetchall()
            
        except:           
            return None
        
        return rs
    
    def close(self):
        self.__conn.close()