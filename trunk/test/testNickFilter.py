# -*- coding: utf8 -*-
import sys
sys.path.append('./src')

import unittest
from futil.foaf.foafAnalyzer import UriLoader
from futil.foaf.nickFilter import NickFilter

from commonFilterTest import CommonFilterTest

class TestNickFilter(CommonFilterTest):

    def testNick(self):

        class NickAnalyzer:
            def run(self, data):
                chain = NickFilter()
                return chain.run(data)

        loader = UriLoader(analyzer=NickAnalyzer())
        foaf = loader.getFoafFrom(self.FRADE)
        self.assertEquals(foaf['nick'], ['Asjastras'])

        foaf = loader.getFoafFrom(self.WIKIER)
        self.assertListEquals(foaf['nick'],['Wikier'])

        foaf = loader.getFoafFrom(self.TRIBES)
        self.assertEquals(foaf['nick'], [])
        foaf = loader.getFoafFrom(self.ECADEMY)
        self.assertEquals(foaf['nick'], ['Debs Tarrier'])
        foaf = loader.getFoafFrom(self.OPERA)
        self.assertEquals(foaf['nick'], ['neonlinux'])

        
if __name__ == "__main__":
  unittest.main()