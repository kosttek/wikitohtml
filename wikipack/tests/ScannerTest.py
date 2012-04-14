'''
Created on 07-04-2012

@author: kosttek
'''
import unittest
import wikipack.scanner.ScannerPack

class TestScanner(unittest.TestCase):
    scanner = 0
    def setUp(self):
        self.scanner= wikipack.scanner.ScannerPack.Scanner()
        self.scanner.loadTree('../data/wikitree2.xml')

    def testScanLineApostroph(self):
        ret = self.scanner.scanLine("ala ma 'kota' ale ''kot'' nie ma '''ali mc bill'''' tak nie \n");
        self.assertEqual(len(ret), 9, "dlugosc listy")
        #TODO rozszerzyc testy 

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
    