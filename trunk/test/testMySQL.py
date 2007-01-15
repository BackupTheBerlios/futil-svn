#!/usr/bin/env python2.4
# -*- coding: utf8 -*-

import sys
sys.path.append('./src')

import unittest
import os
from futil.storage.MySQLWrapper import MySQLWrapper

TESTDB = "foafs-test"
FOAF = 'http://www.wikier.org/foaf.rdf#wikier'

mysql = MySQLWrapper(table=TESTDB)

class TestMySQL(unittest.TestCase):

    def testInsertion(self):
        self.assertTrue(mysql.insert(FOAF))
        self.assertTrue(mysql.exists(FOAF))
        
    def testInsertionDup(self):
        self.assertTrue(mysql.insert(FOAF))
        self.assertFalse(mysql.insert(FOAF))
        
    def testVisit(self):
        mysql.insert(FOAF)
        self.assertFalse(mysql.visited(FOAF))
        mysql.visit(FOAF)
        self.assertTrue(mysql.visited(FOAF))
        
    def testVisitNull(self):
        self.assertFalse(mysql.visited(FOAF))
        
    def testPending(self):
        mysql.insert(FOAF)
        self.assertTrue(mysql.pending())
        
    def testPendingOne(self):
        self.assertTrue(mysql.insert(FOAF))
        self.assertEqual(mysql.getNextPending(), FOAF)
        
    def setUp(self):
        mysql.clean()

    def tearDown(self):
        mysql.clean()

if __name__ == '__main__':
    unittest.main()


