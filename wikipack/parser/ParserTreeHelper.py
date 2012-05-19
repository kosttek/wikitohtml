'''
Created on 19-05-2012

@author: Pepcok
'''
from xml.etree.ElementTree import ElementTree
import os

class ParserTreeHelper(object):
    
    __xmlTreePath = 'parserTree.xml'
    __tokenTree = None


    def __init__(self):
        self.__tokenTree = ElementTree()
        self.__tokenTree.parse(os.path.dirname(__file__) + '\\' + self.__xmlTreePath)
        
    def isTokenATag(self, tokenSymbol):
        tokenList = self.__tokenTree.findall('token')
        for token in tokenList:
            if tokenSymbol == token.find('startTag').text:
                return True
        return False;
    
    def getEndingTag(self, tokenSymbol):
        return None
    
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
   parser = ParserTreeHelper()
   parser.isTokenATag("'''")
