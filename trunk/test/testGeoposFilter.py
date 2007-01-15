# -*- coding: utf8 -*-
import sys
sys.path.append('./src')

import unittest
from futil.foaf.foafAnalyzer import UriLoader
from futil.foaf.geoposFilter import GeoPosFilter

from commonFilterTest import CommonFilterTest

class TestGeoPosFilter(CommonFilterTest):

    def testGeopos(self):
        
        class GeoPosAnalyzer:
            def run(self, data):
                chain = GeoPosFilter()
                return chain.run(data)

        loader = UriLoader(analyzer=GeoPosAnalyzer())
        foaf = loader.getFoafFrom(self.FRADE)
        self.assertEquals(foaf['geolat'], ['43.35401'])
        self.assertEquals(foaf['geolong'],['-5.854694'])

        foaf = loader.getFoafFrom(self.WIKIER)
        self.assertEquals(foaf['geolat'], ['43.437028'])
        self.assertEquals(foaf['geolong'],['-5.77544'])

        foaf = loader.getFoafFrom(self.TRIBES)
        self.assertEquals(foaf['geolat'], ['37.7706'])
        self.assertEquals(foaf['geolong'],['-122.442'])


        foaf = loader.getFoafFrom(self.ECADEMY)
        self.assertEquals(foaf['geolat'], ['51.775'])
        self.assertEquals(foaf['geolong'],['-0.234959'])

        foaf = loader.getFoafFrom(self.OPERA)
        self.assertEquals(foaf['geolat'], ['24.9188094331632'])
        self.assertEquals(foaf['geolong'],['121.285512161161'])
    
        foaf = loader.getFoafFrom(self.NOGEOPOS)
        self.assertFalse(foaf['geolat'], [])        
        self.assertFalse(foaf['geolong'], [])
        
if __name__ == "__main__":
  unittest.main()