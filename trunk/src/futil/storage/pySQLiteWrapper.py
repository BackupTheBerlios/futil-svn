#!/usr/bin/env python2.4
# -*- coding: utf8 -*-

import os
from pysqlite2 import dbapi2 as sqlite
import datetime

class PySQLiteWrapper:

    def __init__(self, path="foaf.db"):
        self.path = path
        if (not os.path.exists(self.path)):
            self.createEmptyDB()
            
    def createEmptyDB(self):
        (con, cur) = self.connect()
        cur.execute("CREATE TABLE foafs (uri TEXT PRIMARY KEY, visited BOOL, date TEXT)")
        con.commit()
        con.close()

    def connect(self):
        connection = sqlite.connect(self.path)
        cursor = connection.cursor()
        return (connection, cursor)

    def query(self, uri):
        con, cur = self.connect()
        query = "SELECT uri FROM foafs WHERE uri =?"
        cur.execute(query, (uri,))
        return cur.fetchmany()


    def insert(self, uri, visited=False):
        if not self.exists(uri):
            date = self.todayDate()
            (con, cur) = self.connect()
            query = """
                        INSERT INTO foafs(uri, visited, date)
                        VALUES ('%s','%s','%s')
                    """ % (uri, visited, date)
            cur.execute(query)
            con.commit()
            return True
        else:
            print "Error: " + uri + " already exists on db"
            return False
            
    def visit(self, uri):
        if self.exists(uri):
            date = self.todayDate()
            (con, cur) = self.connect()
            query = "UPDATE foafs SET visited='True', date='" + date + "' WHERE uri='" + uri + "'"
            cur.execute(query)
            con.commit()
            con.close()
            return True
        else:
            print "Error: " + uri + " not exists on db"
            return False

    def exists(self, uri):
        return (len(self.query(uri)) > 0)
    
    def visited(self, uri):
        con, cur = self.connect()
        query = "SELECT visited FROM foafs WHERE uri =?"
        cur.execute(query, (uri,))
        result = cur.fetchmany()
        if (len(result)>0):
            return self.str2bool(result[0])
        else:
            return False

    def todayDate(self):
        date = datetime.date.today()
        return str(date).replace("-", "")
    
    def str2bool(self, query):
        if (query[0] == 'True'):
            return True
        else:
            return False


