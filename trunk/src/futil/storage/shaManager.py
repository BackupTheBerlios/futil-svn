import os
from pysqlite2 import dbapi2 as sqlite

class ShaManager:
    
    def __init__(self, path="shas.db"):
        self.path = path
        if (not os.path.exists(self.path)):
            self.createEmptyDB()

    def createEmptyDB(self):
        (con, cur) = self.connect()
        cur.execute("CREATE TABLE shas (uri TEXT, sha VARCHAR(40), PRIMARY KEY(uri, sha) )")
        con.commit()
        con.close()
    
    def insertUriSha(self, uri, sha):
        (con, cur) = self.connect()
        query = """
                INSERT INTO shas(uri, sha)
                VALUES ('%s','%s')
            """ % (uri, sha)
        cur.execute(query)
        con.commit()
        con.close() # FIXME 
    
    
    def searchSha(self, sha):
        con, cur = self.connect()
        query = "SELECT uri FROM shas WHERE sha =?"
        cur.execute(query, (sha,))
        result = cur.fetchmany()[:]
        con.close()
        return result
    
    def connect(self):
        connection = sqlite.connect(self.path)
        cursor = connection.cursor()
        return (connection, cursor)
