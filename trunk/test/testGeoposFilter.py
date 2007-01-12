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
        self.assertEquals(foaf['geopos'], [('43.35401','-5.854694')])

        foaf = loader.getFoafFrom(self.WIKIER)
        self.assertListEquals(foaf['geopos'],[("43.437028","-5.77544")])

        foaf = loader.getFoafFrom(self.TRIBES)
        self.assertEquals(foaf['geopos'], [("37.7706","-122.442")])
        foaf = loader.getFoafFrom(self.ECADEMY)
        self.assertEquals(foaf['geopos'], [("51.775","-0.234959")])
        foaf = loader.getFoafFrom(self.OPERA)
        self.assertEquals(foaf['geopos'], [("24.9188094331632","121.285512161161")])

        
if __name__ == "__main__":
  unittest.main()