'''
Created on 20-05-2012

@author: kosttek
'''
from wikipack.scanner.ScannerPack import Scanner
from ParserTreeHelper import ParserTreeHelper
from xml.dom.minidom import Document
from wikipack.parserkostek import ImportModules
from importlib import import_module

class Parser(object):
    tokenList = 0
    count = 0
    parser_tree_helper = ParserTreeHelper()
    doc = Document()
    import_modules = 0
    
    def __init__(self):
        self.import_modules = ImportModules.ImportModules(self)
    
    @staticmethod
    def clearListFromEmptyTokens(tokenList):
        whiteTokensCount = tokenList.count('')
        for i in range(whiteTokensCount):
            tokenList.pop(tokenList.index(''))
        return tokenList
    
    def setTokenList(self, list):
        self.tokenList = list
    
    def parse(self):
        child = self.parseToken("*start",None)
        self.doc.appendChild(child)
    
    def retDoc(self):
        return self.doc
    
    def parseToken(self,startTag, endTag):
        tagName = self.parser_tree_helper.getHTMLTag(startTag)
        retTag = self.doc.createElement(tagName);
        
        inc = 1
        while self.count < len(self.tokenList):
            token = self.tokenList[self.count];
            self.count= self.count + 1
            if self.parser_tree_helper.isTokenATag(token) == True:
                specialTag = self.parser_tree_helper.getSpecTag(token)
                if endTag == token :                 
                    break
                elif specialTag != '' and specialTag != None: 
                    [newToken , inc] = self.import_modules.parse_special(specialTag)
                    self.count= self.count + inc -1 
                    retTag.appendChild(newToken)
                else:
                    
                    newToken = self.parseToken(token , self.parser_tree_helper.getEndingTag(token))
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
    