import ListManager
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element


class Parser(object):
    
    outputFileName = None
    outputFolder = None
    tokenList = None
    
    
    def loadTokenList(self, listWithTokens):
        self.tokenList = listWithTokens
        
    def setOutputFolder(self, _outpuDir):
        self.outputFolder = _outpuDir

    def setOutputFilename(self, _filename):
        self.outputFileName = _filename
        
    def parse(self):
        clearedList = ListManager.ListManager.clearListFromEmptyTokens(self.tokenList)
        #tworzymy head
        mainTree  = ElementTree()
        mainElement = Element()
        lm = ListManager.ListManager()
        lm.loadList(clearedList)
        element = lm.parseListToElement()
        mainElement.append(element)
        
        

if __name__ == '__main__':
    parser = Parser()
    tList = ["", "a", "b", "","c",""]
    parser.loadTokenList(tList)
    parser.parse()
    
 