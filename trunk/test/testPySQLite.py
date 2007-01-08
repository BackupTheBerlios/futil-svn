#!/usr/bin/env python2.4
# -*- coding: utf8 -*-

import sys
sys.path.append('./src')

import unittest
import os
from futil.storage.pySQLiteWrapper import PySQLiteWrapper

TESTDB = "testfoaf.db"
FOAF = 'http://www.wikier.org/foaf.rdf#wikier'

class TestPySQLite(unittest.TestCase):

    def testInsertion(self):
        self.assertTrue(self.pysqlite.insert(FOAF))
        self.assertTrue(self.pysqlite.exists(FOAF))
        
    def testVisit(self):
        self.pysqlite.insert(FOAF)
        self.assertFalse(self.pysqlite.visited(FOAF))
        self.pysqlite.visit(FOAF)
        self.assertTrue(self.pysqlite.visited(FOAF))
        
    def testVisitNull(self):
        self.assertFalse(self.pysqlite.visited(FOAF))
        
    def testPending(self):
        self.pysqlite.insert(FOAF)
        self.assertTrue(self.pysqlite.pending())
        
    def testPending(self):
        self.pysqlite.insert(FOAF)
        self.assertEqual(self.pysqlite.getNextPending(), FOAF)
        
    def setUp(self):
        self.pysqlite = PySQLiteWrapper(TESTDB)

    def tearDown(self):
        os.remove(TESTDB)

if __name__ == '__main__':
    unittest.main()


