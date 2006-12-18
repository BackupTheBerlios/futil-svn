from foaf import Foaf
import unittest

class TestFoaf(unittest.TestCase):


    def setUp(self):
        self._foaf = Foaf('http://frade.no-ip.info:2080/~ivan/foaf.rdf')

    def testCreation(self):
        self.assertEqual(self._foaf.name, "Ivan Frade")
        # sha as string
        self.assertEqual(len(self._foaf.sha), 40)


if __name__ == "__main__":
    unittest.main()
        
