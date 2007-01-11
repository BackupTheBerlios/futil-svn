# -*- coding: utf8 -*-
import sys
sys.path.append('./src')

import rdflib

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

    def testName(self):
        loader = UriLoader()
        foaf = loader.getFoafFrom(FRADE)
        self.assertEquals(foaf['name'], [rdflib.Literal('Ivan Frade')])
        
        foaf = loader.getFoafFrom(WIKIER)
        self.assertEquals(foaf['name'], [rdflib.Literal(u'Sergio Fernández', lang=u'es')])
        
        foaf = loader.getFoafFrom(TRIBES)
        self.assertEquals(foaf['name'], [rdflib.Literal('~*~')])
        foaf = loader.getFoafFrom(ECADEMY)
        self.assertEquals(foaf['name'], [rdflib.Literal('Debbie Tarrier')])
        foaf = loader.getFoafFrom(OPERA)
        self.assertEquals(foaf['name'], [rdflib.Literal(u'Charles McCathieNevile')])

    def testFriends(self):
        loader = UriLoader()
        foaf = loader.getFoafFrom(FRADE)
        self.assertListEquals(foaf['friends'], 
        [ ('98a99390f2fe9395041bddc41e933f50e59a5ecb','http://www.berrueta.net/foaf.rdf'),
          ('97d9756f1281858d0e9e4489003073e4986546ce','http://xtrasgu.asturlinux.org/descargas/foaf.rdf'),
          ('119222cf3a2893a375cc4f884a0138155c771415','http://www.wikier.org/foaf.rdf'),
          ('bd6566af7b3bfa28f917aa545bf4174661817d79','http://www.asturlinux.org/~jsmanrique/foaf.rdf'),
          ('','http://www.kagueto.net/files/foaf.rdf')])

    def assertListEquals(self, obtained, expected):
        self.assertEquals(len(obtained), len(expected), 
                "Different lenght in list of expected and obtained results")
        
        for e in expected:
            if not e in obtained:
                self.assertTrue(False, "Expected " + str(e) + " not in obtained results")
        self.assertTrue(True)
    
if __name__ == "__main__":
  unittest.main()