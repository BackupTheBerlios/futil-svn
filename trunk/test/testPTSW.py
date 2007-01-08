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
        
    def testPingSpecial(self):
        self.assertTrue(self.ptsw.ping("http://www.ecademy.com/module.php?mod=network&op=foafrdf&uid=42059"))
        
    def testParse(self):
        self.assertEquals(len(self.ptsw.parsePinged('data/ptsw-basic.xml')), 1)
        
    def tearDown(self):
        #self.ptsw.printStats()
        pass

if __name__ == "__main__":
    unittest.main()

