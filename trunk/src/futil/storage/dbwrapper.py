#!/usr/bin/env python2.4
# -*- coding: utf8 -*-

class DBWrapper:

    def __init__(self):
        pass
            
    def createEmptyDB(self):
        pass
    
    def connect(self):
        pass

    def query(self, uri):
        pass

    def insert(self, uri, visited=False):
        pass
            
    def visit(self, uri):
        pass

    def exists(self, uri):
        return False
    
    def visited(self, uri):
        return False
        
    def getPending(self):
        pass
    
    def getNextPending(self):
        pass
    
    def pending(self):
        return True
        
    def close(self):
        pass

