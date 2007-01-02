#!/usr/bin/env python2.4
# -*- coding: utf8 -*-

import sys
sys.path.append('./src')

from futil.storage.pySQLiteWrapper import PySQLiteWrapper
import unittest

import os
from pysqlite2 import dbapi2 as sqlite
TESTDB = "testfoaf.db"

class TestPySQLite(unittest.TestCase):

    def testInsertion(self):
        self.assertTrue(self.pysqlite.insert('http://www.wikier.org/foaf.rdf', True))
        self.assertTrue(self.pysqlite.exists('http://www.wikier.org/foaf.rdf'))
        
    def testVisit(self):
        self.pysqlite.insert('http://frade.no-ip.info:2080/~ivan/foaf.rdf', False)
        self.assertTrue(self.pysqlite.visit('http://frade.no-ip.info:2080/~ivan/foaf.rdf'))
        self.assertTrue(self.pysqlite.visited('http://frade.no-ip.info:2080/~ivan/foaf.rdf'))

    def deleteDB(self):
        os.remove(TESTDB)
        

    def setUp(self):
        self.pysqlite = PySQLiteWrapper(TESTDB)

    def tearDown(self):
        self.deleteDB()

if __name__ == '__main__':
    unittest.main()


