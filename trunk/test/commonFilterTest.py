import unittest

class CommonFilterTest(unittest.TestCase):
    
    FRADE = "data/test/frade.rdf"
    WIKIER = "data/test/wikier.rdf"
    TRIBES = "data/test/tribes.rdf"
    ECADEMY = "data/test/ecademy.rdf"
    OPERA = "data/test/opera2.rdf"
    BADXML = "data/test/badxml.rdf"
    
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