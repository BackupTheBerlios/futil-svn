import os
from pysqlite2 import dbapi2 as sqlite

#
# TODO Add a close method and try to keep connection open (performance)
#
class ShaManager:
    
    def __init__(self, path="shas.db"):
        self.connection = None
        self.path = path
        if (not os.path.exists(self.path)):
            self.createEmptyDB()

    def createEmptyDB(self):
        (con, cur) = self.connect()
        cur.execute("CREATE TABLE shas (uri TEXT, sha VARCHAR(40), PRIMARY KEY(uri, sha) )")
        con.commit()
    
    def insertUriSha(self, uri, sha):
        (con, cur) = self.connect()
        query = """
                INSERT INTO shas(uri, sha)
                VALUES ('%s','%s')
            """ % (uri, sha)
        cur.execute(query)
        con.commit()
    
    def searchSha(self, sha):
        con, cur = self.connect()
        query = "SELECT uri,sha FROM shas WHERE sha =?"
        cur.execute(query, (sha,))
        result = cur.fetchmany()[:]
        return [uri for uri,sha in result]
    
    def connect(self):
        if not self.connection:
            self.connection = sqlite.connect(self.path)
        cursor = self.connection.cursor()
        return (self.connection, cursor)

    def printDatabase(self):
        con, cur = self.connect()
        query = "SELECT * FROM shas"
        cur.execute(query, ())
        result = cur.fetchmany()[:]
        return result
    
    def close(self):
        self.connection.close()