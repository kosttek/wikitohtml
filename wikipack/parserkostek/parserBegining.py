'''
Created on 20-05-2012

@author: kosttek
'''
from wikipack.scanner.ScannerPack import Scanner
from ParserTreeHelper import ParserTreeHelper
from xml.dom.minidom import Document

class Parser(object):
    tokenList = 0
    count = 0
    parserTreeHelper = ParserTreeHelper()
    doc = Document()
    @staticmethod
    def clearListFromEmptyTokens(tokenList):
        whiteTokensCount = tokenList.count('')
        for i in range(whiteTokensCount):
            tokenList.pop(tokenList.index(''))
        return tokenList
    
    def setTokenList(self, list):
        self.tokenList = list
    
    def parse(self):
        child = self.parseToken("*start","")
        self.doc.appendChild(child)
    
    def retDoc(self):
        return self.doc
    
    def parseToken(self,startTag, endTag):
        tagName = self.parserTreeHelper.getHTMLTag(startTag)
        retTag = self.doc.createElement(tagName);
        while self.count < len(self.tokenList):
            token = self.tokenList[self.count];
            
            self.count= self.count +1 
            
            if self.parserTreeHelper.isTokenATag(token) == True:
                if endTag == token :
                    return retTag
                else:
                    newToken = self.parseToken(token , self.parserTreeHelper.getEndingTag(token))
                    retTag.appendChild(newToken);
            else:
                ptext = self.doc.createTextNode(token)
                retTag.appendChild(ptext)
        return retTag


if __name__ == '__main__':
    scanner = Scanner()
    scanner.loadTree('../data/wikitree2.xml')
    scanner.loadFile('../data/testfile')
    result = scanner.scan()
    Parser.clearListFromEmptyTokens(result)
    parser = Parser()
    parser.setTokenList(result)
    parser.parse()
    print result
    docc = parser.retDoc()
    print docc.toprettyxml(indent="  ")
    