import os
from pysqlite2 import dbapi2 as sqlite

#
# TODO Add a close method and try to keep connection open (performance)
#
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
        query = "SELECT uri,sha FROM shas WHERE sha =?"
        cur.execute(query, (sha,))
        result = cur.fetchmany()[:]
        con.close()
        return [uri for uri,sha in result]
    
    def connect(self):
        connection = sqlite.connect(self.path)
        cursor = connection.cursor()
        return (connection, cursor)

    def printDatabase(self):
        con, cur = self.connect()
        query = "SELECT * FROM shas"
        cur.execute(query, ())
        result = cur.fetchmany()[:]
        con.close
        return result