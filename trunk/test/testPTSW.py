#!/usr/bin/env python2.4
# -*- coding: utf8 -*-
import sys
sys.path.append('./src')

from futil.utils.ptsw import PTSW
import unittest

ptsw = PTSW()

class TestPTSW(unittest.TestCase):

    def setUp(self):
        pass

    def testPing(self):
        self.assertTrue(ptsw.ping("http://www.wikier.org/foaf.rdf#wikier"))
        
    def testPingSpecial(self):
        self.assertTrue(ptsw.ping("http://www.ecademy.com/module.php?mod=network&op=foafrdf&uid=42059"))
        
    def testParse(self):
        self.assertEquals(len(ptsw.parsePinged('data/ptsw-basic.xml')), 1)
        
    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()

