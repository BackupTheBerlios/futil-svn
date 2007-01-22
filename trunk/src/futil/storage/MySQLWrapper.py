#!/usr/bin/env python2.4
# -*- coding: utf8 -*-

import os, sys
from futil.storage.dbwrapper import DBWrapper
import MySQLdb
from futil.utils.logger import FutilLogger

CACHE = 100

class MySQLWrapper(DBWrapper):

    def __init__(self, app='futil', host='localhost', db='futil', user='futil', passwd='futil', table='foafs'):
        self.data = { 'host':host, 'db':db, 'user':user, 'passwd':passwd, 'table':table}
        self.connection = None
        self.log = FutilLogger(app)
        self.pendingCache = []

    def realConnect(self):
        try:
            return MySQLdb.connect(host=self.data['host'], db=self.data['db'],
                                   user=self.data['user'], passwd=self.data['passwd']) 
        except MySQLdb.Error, e:
            self.log.error('conecting to db: ' + str(e[1]))
            sys.exit(-1)
    
    def connect(self):
        if (self.connection==None):
            self.connection = self.realConnect()
        return (self.connection, self.connection.cursor())

    def query(self, uri):
        con, cur = self.connect()
        query = "SELECT uri FROM `"+self.data['table']+"` WHERE uri='"+uri+"';"
        cur.execute(query)
        return cur.fetchall()

    def insert(self, uri, visited=False):
        visited = int(visited)
        date = self.todayDate()
        (con, cur) = self.connect()
        query = "INSERT INTO `"+self.data['table']+"` (uri, visited, date) VALUES ('"+uri+"',"+str(visited)+","+date+")"
        try:
            cur.execute(query)
            return True
        except MySQLdb.IntegrityError, details:
            self.log.warn(uri + ' already exists on db')
            return False
        except AssertionError, details:
            self.log.error('inserting ' + uri + ': ' + str(details))
            return False
        except Exception, details:
            self.log.error('inserting ' + uri + ': ' + str(details))
            return False
            
    def visit(self, uri):
        if self.exists(uri):
            date = self.todayDate()
            (con, cur) = self.connect()
            query = "UPDATE `" + self.data['table'] + "` SET visited=1, date='" + date + "' WHERE uri='" + uri + "'"
            cur.execute(query)
            return True
        else:
            self.log.error(uri + ' not exists on db')
            return False

    def exists(self, uri):
        return (len(self.query(uri)) > 0)
    
    def visited(self, uri):
        con, cur = self.connect()
        query = "SELECT visited FROM `"+self.data['table']+"` WHERE uri ='" + uri + "' AND visited=1"
        cur.execute(query)
        result = cur.fetchall()
        return (len(result)>0)
        
    def getPending(self):
        con, cur = self.connect()
        query = "SELECT uri FROM `"+self.data['table']+"` WHERE visited=0"
        cur.execute(query)
        results = []
        for result in cur.fetchall():
            results.append(result)
        return results
        
    
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
    
    def clean(self):
        con, cur = self.connect()
        query = "delete from `" + self.data['table'] + "`;"
        cur.execute(query)
        
    def close(self):
        if (self.connection != None):
            self.connection.close()


