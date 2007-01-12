# -*- coding: utf8 -*-
import sys
sys.path.append('./src')

import rdflib

import unittest
from futil.foaf.foafAnalyzer import UriLoader
from commonFilterTest import CommonFilterTest

class TestFoaf(CommonFilterTest):

    def testAnalyzer(self):
        """
            Test complete analyze process
        """
        loader = UriLoader()
        foaf = loader.getFoafFrom(self.FRADE)
        self.assertEquals(foaf['name'], [rdflib.Literal('Ivan Frade')])
        self.assertEquals(foaf['sha'], [u'84d076726727b596b08198e26ef37e4817353e97'])
        self.assertListEquals(foaf['friends'], 
        [ ('98a99390f2fe9395041bddc41e933f50e59a5ecb','http://www.berrueta.net/foaf.rdf'),
          ('97d9756f1281858d0e9e4489003073e4986546ce','http://xtrasgu.asturlinux.org/descargas/foaf.rdf'),
          ('119222cf3a2893a375cc4f884a0138155c771415','http://www.wikier.org/foaf.rdf'),
          ('bd6566af7b3bfa28f917aa545bf4174661817d79','http://www.asturlinux.org/~jsmanrique/foaf.rdf'),
          ('','http://www.kagueto.net/files/foaf.rdf')])
        self.assertEquals(foaf['geopos'], [('43.35401','-5.854694')])
        self.assertEquals(foaf['nick'], ['Asjastras'])
        print foaf

if __name__ == "__main__":
  unittest.main()