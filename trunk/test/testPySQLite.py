#!/usr/bin/env python2.4
# -*- coding: utf8 -*-

import sys
sys.path.append('./src')

import unittest
import os
from futil.storage.pySQLiteWrapper import PySQLiteWrapper

TESTDB = "testfoaf.db"
FOAFS = ['http://www.wikier.org/foaf.rdf#wikier',
         'http://frade.no-ip.info:2080/~ivan/foaf.rdf',
         'http://www.berrueta.net/foaf.rdf#me'
         ]

class TestPySQLite(unittest.TestCase):

    def testInsertion(self):
        self.assertTrue(self.pysqlite.insert(FOAFS[0]))
        self.assertTrue(self.pysqlite.exists(FOAFS[0]))
        
    def testVisit(self):
        self.pysqlite.insert(FOAFS[1])
        self.assertFalse(self.pysqlite.visited(FOAFS[1]))
        self.pysqlite.visit(FOAFS[1])
        self.assertTrue(self.pysqlite.visited(FOAFS[1]))
        
    def testVisitNull(self):
        self.assertFalse(self.pysqlite.visited(FOAFS[2]))
        
    def testPending(self):
        self.pysqlite.insert(FOAFS[2])
        self.assertTrue(self.pysqlite.pending())
        
    def setUp(self):
        self.pysqlite = PySQLiteWrapper(TESTDB)

    def tearDown(self):
        os.remove(TESTDB)

if __name__ == '__main__':
    unittest.main()


