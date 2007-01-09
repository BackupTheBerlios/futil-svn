#!/usr/bin/env python2.4
# -*- coding: utf8 -*-

import datetime

class DBWrapper:

    def __init__(self):
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
    
    def todayDate(self):
        date = datetime.date.today()
        return str(date).replace("-", "")
        
    def close(self):
        pass

