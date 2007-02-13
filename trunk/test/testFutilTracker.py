#!/usr/bin/env python2.4
# -*- coding: utf8 -*-

import sys, os
sys.path.append('./src')

from futil.tracker.futiltracker import FutilTracker
import unittest

TESTDB = "foafs-test"
FOAFS = ['http://www.wikier.org/foaf.rdf#wikier',
         'http://frade.no-ip.info:2080/~ivan/foaf.rdf'
         ]

class TestFutilTracker(unittest.TestCase):

    def testEmpty(self):
        self.assertFalse(self.ft.moreUrisToExplore())
        
    def testPut(self):
        self.ft.putFriendsUris(FOAFS)
        self.assertTrue(self.ft.moreUrisToExplore())
        self.ft.getNextUri()
        self.assertTrue(self.ft.moreUrisToExplore())
        self.ft.getNextUri()
        self.assertFalse(self.ft.moreUrisToExplore())
        
    def setUp(self):
        self.ft = FutilTracker(TESTDB)        
        
    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()