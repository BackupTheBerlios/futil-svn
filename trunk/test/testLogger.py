#!/usr/bin/env python2.4
# -*- coding: utf8 -*-
import sys
sys.path.append('./src')

from futil.utils.logger import FutilLogger
import unittest

log = FutilLogger('logger-test')

class TestPTSW(unittest.TestCase):

    def setUp(self):
        pass

    def testInfo(self):
        log.info('testing')
        
    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()