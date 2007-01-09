import sys
sys.path.append('./src')

import unittest

TRIBES = "data/test/tribes.rdf"

##class Foaf:
##    def __init__(self, filename):
##        analyzer = FoafAnalyzer()
##        self.__dict__ = analyzer.getFoaf(filename)

class TestFoaf(unittest.TestCase):

    def testTribes(self):
        print TRIBES
        self.assertEquals(TRIBES, TRIBES)



if __name__ == "__main__":
  unittest.main()