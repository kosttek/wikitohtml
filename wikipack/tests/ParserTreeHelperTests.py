'''
Created on 19-05-2012

@author: Pepcok
'''
import unittest
from wikipack.parser.ParserTreeHelper import ParserTreeHelper

class ParserTreeHelperTests(unittest.TestCase):

    emptyTokenTag = ""

    def setUp(self):
        self.pth = ParserTreeHelper()

    #tag Valdetion

    def testValidTag(self):
        validTokenTag = "'''"
        
        self.assertTrue(self.pth.isTokenATag(validTokenTag), 'Tag should be marked as Tag Token')
    
    def testInvalidTag(self):
        invalidTokenTag = "Just a simple text"
        
        self.assertFalse(self.pth.isTokenATag(invalidTokenTag), 'Tag is invalid and should NOT be marked as Tag Token')
    
    def testEmptyTag(self):
        
        self.assertFalse(self.pth.isTokenATag(self.emptyTokenTag), 'Tag is empty and should NOT be marked as Tag Token')
        
        
    #getEndingTag method    
        
    def testGettingEndingTagWithEmptyToken(self):

        self.assertEqual(self.pth.getEndingTag(self.emptyTokenTag), None, 'Result is not None')
    
    def testGettingEndingTagWithValidToken(self):
        validSimpleTag = "'''"
        
        self.assertEqual(self.pth.getEndingTag(validSimpleTag), "'''", 'Returned token is not valid')

    def testGettingEndingTagWithInvalidToken(self):
        invalidTag = "blabla"
        
        self.assertEqual(self.pth.getEndingTag(invalidTag), None, 'Invalid token did not return none')
        
    #getTagId method
    
    def testGettingTagIdWithEmptyToken(self):
        emptyTokenTag = ""
        returnedValue = self.pth.getTagId(emptyTokenTag)
        expectedValue = None
        
        self.assertEqual(returnedValue, expectedValue, 'Empty token did not return None')
        
    def testGettingTagIdWithValidToken(self):
        validTokenTag = "'''"
        returnedValue = self.pth.getTagId(validTokenTag)
        expectedValue = 'bold'
        
        self.assertEqual(returnedValue, expectedValue, 'Valid token returned wrong value')
            
    def testGettingTagIdWithInvalidToken(self):
        invalidTokenTag = "i'n'v"
        returnedValue = self.pth.getTagId(invalidTokenTag)
        expectedValue = None
        
        self.assertEqual(returnedValue, expectedValue, 'Empty token did not return None')
        
    def testAffectingLineWithInvalidToken(self):
        invalidToken = "a"
        returnedValue = self.pth.affectsLine(invalidToken)
        expectedValue = False
        
        self.assertEqual(returnedValue, expectedValue, 'Invalid affecting token did not return None')
        
    def testAffectingLineWithValidToken(self):
        validToken = ";"
        returnedValue = self.pth.affectsLine(validToken)
        expectedValue = True
        
        self.assertEqual(returnedValue, expectedValue, 'Invalid affecting token did not return True')
        
if __name__ == "__main__":
    
    
    #import sys;sys.argv = ['', 'Test.testValidTag']
    unittest.main()