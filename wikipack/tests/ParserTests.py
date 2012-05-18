'''
Created on 26-04-2012

@author: Pepcok
'''
import unittest
import wikipack.scanner
import wikipack.parser
import wikipack.fileLoader
import os
import filecmp

class Test(unittest.TestCase):
    
    fileLoader = None
    scanner = None
    parser = None
    temporaryOutputDir = None
    def setUp(self):
#        unittest.TestCase.setUp(self)
        self.fileLoader = wikipack.fileLoader.fileLoader()
        self.scanner = wikipack.scanner.ScannerPack.Scanner()
        self.praser = wikipack.parser.Parser()
        self.temporaryOutputDir = 'PepcokTests/outputTemporaryFiles/'
        self.outputDirWithValidFiles = 'PepcokTests/outputTestFiles/'
    
    def tearDown(self):
        folder = 'PepcokTests/outputTemporaryFiles/'
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            print file_path
#            try:
#                if os.path.isfile(file_path):
#                    os.unlink(file_path)
#            except Exception, e:
#                print e
        
    def testBold(self):
        fileName= 'boldTest'
        
        self.fileLoader.loadFile(fileName)
        fContent = self.fileLoader.getFileContent()
        listWithTokens = self.scanner.scanLine(fContent)
        self.parser.loadTokenList(listWithTokens)
        self.parser.setOutputFolder(self.temporaryOutputDir)
        self.parser.setOutputFilename(fileName)
        
        self.parser.parse()
        
        self.assertTrue(os.path.isfile(self.temporaryOutputDir + fileName))
        self.assertEqual(filecmp.cmp(self.outputDirWithValidFiles + fileName +'.xml', self.temporaryOutputDir + fileName + '.xml'))
        
        
class TokenListManger:
    tokenList = None
    
    def __init__(self, _tokenList):
        self.tokenList = _tokenList

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()