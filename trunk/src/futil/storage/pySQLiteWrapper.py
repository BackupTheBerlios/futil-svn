#!/usr/bin/env python2.4
# -*- coding: utf8 -*-

import os
from pysqlite2 import dbapi2 as sqlite
import datetime
from futil.utils.logger import FutilLogger

CACHE = 100

class PySQLiteWrapper:

    def __init__(self, path="foaf.db"):
        self.path = path
        self.connection = None
        if (not os.path.exists(self.path)):
            self.createEmptyDB()
        self.log = FutilLogger()
        self.pendingCache = []
            
    def createEmptyDB(self):
        (con, cur) = self.connect()
        cur.execute("CREATE TABLE foafs (uri TEXT PRIMARY KEY, visited BOOL, date TEXT)")
        con.commit()

    def realConnect(self):
        return sqlite.connect(self.path)
    
    def connect(self):
        if (self.connection==None):
            self.connection = self.realConnect()
        return (self.connection, self.connection.cursor())

    def query(self, uri):
        con, cur = self.connect()
        query = "SELECT uri FROM foafs WHERE uri =?"
        cur.execute(query, (uri,))
        return cur.fetchall()

    def insert(self, uri, visited=False):
        if not self.exists(uri):
            date = self.todayDate()
            (con, cur) = self.connect()
            query = """
                        INSERT INTO foafs(uri, visited, date)
                        VALUES ('%s','%s','%s')
                    """ % (uri, visited, date)
            try:
                cur.execute(query)
                con.commit()
                return True
            except:
                self.log.info('Error inserting: ' + uri)
                return False
        else:
            self.log.info('Error: ' + uri + ' already exists on db')
            return False
            
    def visit(self, uri):
        if self.exists(uri):
            date = self.todayDate()
            (con, cur) = self.connect()
            query = "UPDATE foafs SET visited='True', date='" + date + "' WHERE uri='" + uri + "'"
            cur.execute(query)
            con.commit()
            return True
        else:
            self.log.info('Error: ' + uri + ' not exists on db')
            return False

    def exists(self, uri):
        return (len(self.query(uri)) > 0)
    
    def visited(self, uri):
        con, cur = self.connect()
        query = "SELECT visited FROM foafs WHERE uri =?"
        cur.execute(query, (uri,))
        result = cur.fetchall()
        if (len(result)>0):
            return self.str2bool(result[0])
        else:
            return False
        
    def getPending(self):
        con, cur = self.connect()
        query = "SELECT uri FROM foafs WHERE visited='False'"
        cur.execute(query)
        return cur.fetchall()
    
    def getNextPending(self):
        if (len(self.pendingCache) == 0):
            pending = self.getPending()
            pendingSize = len(pending)
            self.log.info(str(pendingSize) + ' URIs pending to visit')
            if (pendingSize > CACHE):
                self.pendingCache = pending[:CACHE]
            else:
                self.pendingCache = pending
                
        return self.pendingCache.pop()[0]
    
    def pending(self):
        return (len(self.getPending())>0)

    def todayDate(self):
        date = datetime.date.today()
        return str(date).replace("-", "")
    
    def str2bool(self, query):
        if (query[0] == 'True'):
            return True
        else:
            return False
        
    def __del__(self):
        if (self.connection != None):
            self.connection.close()


