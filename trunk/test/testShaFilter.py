# -*- coding: utf8 -*-
import sys
sys.path.append('./src')

import rdflib
import unittest
from futil.foaf.foafAnalyzer import UriLoader
from futil.foaf.shaFilter import ShaFilter

from commonFilterTest import CommonFilterTest

class TestShaFilter(CommonFilterTest):

    def testSha(self):

        class ShaAnalyzer:
            def run(self, data):
                chain = ShaFilter()
                return chain.run(data)

        loader = UriLoader(analyzer=ShaAnalyzer())
        foaf = loader.getFoafFrom(self.FRADE)
        self.assertEquals(foaf['sha'], [u'84d076726727b596b08198e26ef37e4817353e97'])

        foaf = loader.getFoafFrom(self.WIKIER)
        self.assertListEquals(foaf['sha'], [u'd0fd987214f56f70b4c47fb96795f348691f93ab',
                                    u'a087165d16083deb201734af4dec2d64a40236fc',
                                    u'119222cf3a2893a375cc4f884a0138155c771415',
                                    u'3bb939b9fe7a4e45ec9d65d64074c3b2a4ce317d'])

        foaf = loader.getFoafFrom(self.TRIBES)
        self.assertEquals(foaf['sha'], ['c4ae9b8c2ba7361e8697db0c6ba7c08417bd6101'])
        foaf = loader.getFoafFrom(self.ECADEMY)
        self.assertEquals(foaf['sha'], [u'd1c29956cac7a2b4ac5e48e387452d6c61df1f61'])
        foaf = loader.getFoafFrom(self.OPERA)
        self.assertEquals(foaf['sha'], [u'819a368bea77c9ece2f4af144e1a60ccfce4e376'])

        
if __name__ == "__main__":
  unittest.main()