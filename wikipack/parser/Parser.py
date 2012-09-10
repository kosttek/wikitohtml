import ListManager
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
from xml.dom import minidom
from wikipack.parser.wikiparser import wikify
from xml.etree.ElementTree import tostring

class Parser(object):
    
    outputFileName = None
    outputFolder = None
    tokenList = None
    options = None
    
    
    def loadTokenList(self, listWithTokens, opitons):
        self.tokenList = listWithTokens
        self.options = opitons
        
    def setOutputFolder(self, _outpuDir):
        self.outputFolder = _outpuDir

    def setOutputFilename(self, _filename):
        self.outputFileName = _filename
        
    def parse(self):
        clearedList = ListManager.ListManager.clearListFromEmptyTokens(self.tokenList)
        #tworzymy head
        mainTree  = ElementTree()
        mainElement = Element("parserTreeHead")
        mainTree._setroot(mainElement)
        lm = ListManager.ListManager()
        lm.loadList(clearedList)
        
#        lm.parseListToElement()
#        tostring(mainElement)

        element = lm.parseListToElement()
        mainElement.append(element)
        wikify(None, self.options)
        
#        ElementTree(mainElement).write('file.xml')
if __name__ == '__main__':
    parser = Parser()
#    tList = ["", "a", "b", "","c","","q","abcde","tekst", "w"]
#    tList = ["", "a", "b", "","c","","'''","abcde","tekst", "'''"]
    tList = ["'''", "a", "1", "'''", "b", "'''", "c", ';', 'a', 'b', '\n', ';', 'c', 'd', 'e', 'f', '[[', 'abcd', 'cde', ']]', 'xyz']
    parser.loadTokenList(tList)
    parser.parse()