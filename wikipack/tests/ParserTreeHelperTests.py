'''
Created on 19-05-2012

@author: Pepcok
'''
import unittest
from wikipack.parser.ParserTreeHelper import ParserTreeHelper

class ParserTreeHelperTests(unittest.TestCase):

    def setUp(self):
        self.pth = ParserTreeHelper()

    def testValidTag(self):
        validTokenTag = "'''"
        
        self.assertTrue(self.pth.isTokenATag(validTokenTag), 'Tag should be marked as Tag Token')
    
    def testInvalidTag(self):
        invalidTokenTag = "Just a simple text"
        
        self.assertFalse(self.pth.isTokenATag(invalidTokenTag), 'Tag is invalid and should NOT be marked as Tag Token')
    
    def testEmptyTag(self):
        emptyTokenTag = ""
        
        self.assertFalse(self.pth.isTokenATag(emptyTokenTag), 'Tag is empty and should NOT be marked as Tag Token')
        
    def testGettingEndingTagWithEmptyToken(self):
        emptyTokenTag = ""
        
        self.assertEqual(self.pth.getEndingTag(emptyTokenTag), None, 'Result is not None')
    
    def testGettingEndingTagWithValidToken(self):
        validSimpleTag = "'''"
        
        self.assertEqual(self.pth.getEndingTag(validSimpleTag), "'''", 'Returned token is not valid')

    def testGettingEndingTagWithInvalidToken(self):
        invalidTag = "blabla"
        
        self.assertEqual(self.pth.getEndingTag(invalidTag), None, 'Invalid token did not return none')
        
if __name__ == "__main__":
    
    
    #import sys;sys.argv = ['', 'Test.testValidTag']
    unittest.main()