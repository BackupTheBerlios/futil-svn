import os
from pysqlite2 import dbapi2 as sqlite

from futil.utils.logger import FutilLogger

#
# TODO Add a close method and try to keep connection open (performance)
#
class ShaManager:

    def __init__(self, path='shas.db', app='futil'):
        self._logger = FutilLogger(app)
        self.connection = None
        self.path = path
        if (not os.path.exists(self.path)):
            self.createEmptyDB()

    def createEmptyDB(self):
        (con, cur) = self.connect()
        cur.execute("CREATE TABLE shas (uri TEXT, sha VARCHAR(40), PRIMARY KEY(uri, sha) )")
        con.commit()

    def insertUriSha(self, uri, sha):
        try:
            (con, cur) = self.connect()
            query = """
                    INSERT INTO shas(uri, sha)
                    VALUES ('%s','%s')
                """ % (uri, sha)
            cur.execute(query)
            con.commit()
        except Exception, e:
            self._logger.error("Inserting in sha database " + str(e))
            pass

    def searchSha(self, sha):
        con, cur = self.connect()
        query = "SELECT uri,sha FROM shas WHERE sha =?"
        cur.execute(query, (sha,))
        result = cur.fetchmany()[:]
        return [uri for uri,sha in result]

    def connect(self):
        if not self.connection:
            self.connection = sqlite.connect(self.path)
        try:
            cursor = self.connection.cursor()
        except:
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
        if self.connection:
            self.connection.close()