#!/usr/bin/env python2.4
# -*- coding: utf8 -*-

from ptsw import PTSW
import unittest

class TestPTSW(unittest.TestCase):

    def setUp(self):
        self.ptsw = PTSW()

    def testPing(self):
        self.assertTrue(self.ptsw.ping("http://www.wikier.org/foaf.rdf#wikier"))

if __name__ == "__main__":
    unittest.main()
        
