#!/usr/bin/env python2.4
# -*- coding: utf8 -*-
import sys
sys.path.append('./src')

from futil.utils.ptsw import PTSW
import unittest

class TestPTSW(unittest.TestCase):

    def setUp(self):
        self.ptsw = PTSW()

    def testPing(self):
        self.assertTrue(self.ptsw.ping("http://www.wikier.org/foaf.rdf#wikier"))
        
    def testParse(self):
        self.assertEquals(len(self.ptsw.parsePinged('data/ptsw-basic.xml')), 1)

if __name__ == "__main__":
    unittest.main()

