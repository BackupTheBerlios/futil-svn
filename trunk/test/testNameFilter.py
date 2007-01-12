# -*- coding: utf8 -*-
import sys
sys.path.append('./src')

import rdflib
import unittest
from futil.foaf.foafAnalyzer import UriLoader
from futil.foaf.nameFilter import NameFilter

from commonFilterTest import CommonFilterTest

class TestNameFilter(CommonFilterTest):

    def testName(self):

        class NameAnalyzer:
            def run(self, data):
                chain = NameFilter()
                return chain.run(data)

        loader = UriLoader(analyzer=NameAnalyzer())
        loader = UriLoader()
        foaf = loader.getFoafFrom(self.FRADE)
        self.assertEquals(foaf['name'], [rdflib.Literal('Ivan Frade')])
        
        foaf = loader.getFoafFrom(self.WIKIER)
        self.assertEquals(foaf['name'], [rdflib.Literal(u'Sergio Fernández', lang=u'es')])
        
        foaf = loader.getFoafFrom(self.TRIBES)
        self.assertEquals(foaf['name'], [rdflib.Literal('~*~')])
        foaf = loader.getFoafFrom(self.ECADEMY)
        self.assertEquals(foaf['name'], [rdflib.Literal('Debbie Tarrier')])
        foaf = loader.getFoafFrom(self.OPERA)
        self.assertEquals(foaf['name'], [])


if __name__ == "__main__":
  unittest.main()