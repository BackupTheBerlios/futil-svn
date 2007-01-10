import sys
sys.path.append('./src')

import unittest
from futil.foaf.foafAnalyzer import UriLoader

FRADE = "data/test/frade.rdf"
WIKIER = "data/test/wikier.rdf"
TRIBES = "data/test/tribes.rdf"
ECADEMY = "data/test/ecademy.rdf"
OPERA = "data/test/opera.rdf"


class TestFoaf(unittest.TestCase):

    def testSha(self):
        loader = UriLoader()
        foaf = loader.getFoafFrom(FRADE)
        self.assertEquals(foaf['sha'], [u'84d076726727b596b08198e26ef37e4817353e97'])

        foaf = loader.getFoafFrom(WIKIER)
        self.assertEquals(foaf['sha'], [u'd0fd987214f56f70b4c47fb96795f348691f93ab',
                                    u'a087165d16083deb201734af4dec2d64a40236fc',
                                    u'119222cf3a2893a375cc4f884a0138155c771415',
                                    u'3bb939b9fe7a4e45ec9d65d64074c3b2a4ce317d'])

        foaf = loader.getFoafFrom(TRIBES)
        self.assertEquals(foaf['sha'], ['c4ae9b8c2ba7361e8697db0c6ba7c08417bd6101'])
        foaf = loader.getFoafFrom(ECADEMY)
        self.assertEquals(foaf['sha'], [u'd1c29956cac7a2b4ac5e48e387452d6c61df1f61'])
        foaf = loader.getFoafFrom(OPERA)
        self.assertEquals(foaf['sha'], [u'db161c28da4ac9c8b284ba9a146b09e3899554d5'])



if __name__ == "__main__":
  unittest.main()