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
        
        foaf = loader.getFoafFrom(WIKIER)        
        self.assertListEquals(foaf['friends'],
            [('057048f30557d8e26f71fdec6ef43542166ca932', u'http://www.ivanminguez.net/foaf.rdf'), 
             ('84d076726727b596b08198e26ef37e4817353e97', u'http://frade.no-ip.info:2080/~ivan/foaf.rdf'), 
             ('3d0a8f16ce3d560ca75e16d36f6ded63599c60a7', u'http://www.di.uniovi.es/~labra/labraFoaf.rdf'), 
             ('3665f4f2370ddd6358da4062f3293f6dc7f39b7c', u'http://eikeon.com/foaf.rdf'), 
             ('135a617c9e2e37003e1c38be6c21ce7af433552f', u'http://petra.euitio.uniovi.es/~i1637566/foaf.rdf'), 
             ('eb6d13cb99da7b9895030f4c2f22286a18d23442', u'http://aleasoft.hopto.org/~alvaro/weblog/foaf.rdf'), 
             ('0ca8d97a347deaf776a0d0967dba48c571c3dd09', u'http://koalazoo.wikier.org/foaf.rdf'), 
             ('bd6566af7b3bfa28f917aa545bf4174661817d79', u'http://www.asturlinux.org/~jsmanrique/foaf.rdf'), 
             ('56e6f2903933a611708ebac456d45e454ddb8838', u'http://captsolo.net/semweb/foaf-captsolo.rdf'),
             ('97d9756f1281858d0e9e4489003073e4986546ce', u'http://xtrasgu.asturlinux.org/descargas/foaf.rdf'), 
             ('98a99390f2fe9395041bddc41e933f50e59a5ecb', u'http://www.berrueta.net/foaf.rdf#me'), 
             ('3d23bbb5b37a688d9c7fa781844d52d248b47ceb', u'http://www.w3c.es/Personal/Martin/foaf.rdf'), 
             ('9a6b7eefc08fd755d51dd9321aecfcc87992e9a2', u'http://www.johnbreslin.com/foaf/foaf.rdf'), 
             ('6b31c41e80d36cc08a489462c0c2c37d7de8d2e5', u'http://criptonita.com/~nacho/foaf.rdf'), 
             ('0363c58a9ec61db68e3fa37cfcd38b301deaab97', u'http://www.kagueto.net/files/foaf.rdf')])


##
##    FIXME Implement test cases
##
##        self.assertEquals(foaf['name'], [rdflib.Literal('~*~')])
##        foaf = loader.getFoafFrom(ECADEMY)
##        self.assertEquals(foaf['name'], [rdflib.Literal('Debbie Tarrier')])
##        foaf = loader.getFoafFrom(OPERA)
##        self.assertEquals(foaf['name'], [rdflib.Literal(u'Charles McCathieNevile')])


            
    def assertListEquals(self, obtained, expected):
        self.assertEquals(len(obtained), len(expected), 
                "Different lenght in list of expected and obtained results")
         
        for e in expected:
            if not e in obtained:
                self.assertTrue(False, "Expected " + str(e) + " not in obtained results")
        self.assertTrue(True)
    
    def diffList(self, list1, list2):
        only1 = [l for l in list1 if not l in list2]
        only2 = [l for l in list2 if not l in list1]
        print only1
        print " * * * * * * * "
        print only2
        
if __name__ == "__main__":
  unittest.main()