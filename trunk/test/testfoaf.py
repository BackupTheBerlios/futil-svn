import sys
sys.path.append('./src')

from futil.foaf.foaf import Foaf
import unittest

from rdflib.Literal import Literal

class TestFoaf(unittest.TestCase):

    def setUp(self):
        self._foaf = Foaf('http://frade.no-ip.info:2080/~ivan/foaf.rdf')

    def testCreation(self):
        self.assertEqual(self._foaf.name[0], Literal("Ivan Frade"))
        # sha as string
        self.assertEqual(len(self._foaf.sha[0]), 40)


if __name__ == "__main__":
    unittest.main()
