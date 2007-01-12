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
OPERA = "data/test/opera2.rdf"


class TestFoaf(unittest.TestCase):

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
        self.assertEquals(foaf['name'], [])

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

        foaf = loader.getFoafFrom(TRIBES)
        self.assertEquals(len(foaf['friends']), 485)
        foaf = loader.getFoafFrom(ECADEMY)
        self.assertEquals(len(foaf['friends']), 267)
        foaf = loader.getFoafFrom(OPERA)
        self.assertListEquals(foaf['friends'], 
        [('1d69281af85b84cd835ab50bcf4ef2dcb2369175', u'http://my.opera.com/sparklecitygirl/xml/foaf'), 
            ('c6ae1fdfe38a26a7ada2dc3cce523d9153f7cb00', u'http://my.opera.com/kutch_hariompariwar/xml/foaf'), 
            ('cad5eaac9ea250c47c63384f04810bb4dd3c9b33', u'http://my.opera.com/six_string_wizard/xml/foaf'),
            ('f09f0562d95fbb230d95c2ca3eee557a6a3bdc38', u'http://my.opera.com/mimag/xml/foaf'), 
            ('cdaa6158e4d46c0bb5eeedd74e53247db8fb27b8', u'http://my.opera.com/seifip/xml/foaf'), 
            ('31441e1cd62c38dd41e883bc4ac540d6c6c77d23', u'http://my.opera.com/honeybe/xml/foaf'), 
            ('242e339959af5a23da371ffa43f429eabf8a489e', u'http://my.opera.com/chinajon/xml/foaf'),
            ('3343e5aadc080b4a413220be2443c0bdc762b3df', u'http://my.opera.com/Nyingje/xml/foaf'),
            ('b15d7e177925df04a76abb0714877640ad8495c1', u'http://my.opera.com/zenya/xml/foaf'), 
            ('ec65076a7228f613e3f1b0cf27661395299ca14d', u'http://my.opera.com/SerbianFighter/xml/foaf')])
        


            
    def assertListEquals(self, obtained, expected):
        self.assertEquals(len(obtained), len(expected), "Different lenght in list of expected and obtained results")
         
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