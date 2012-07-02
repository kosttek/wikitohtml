import ListManager
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
from xml.dom import minidom
from xml.etree.ElementTree import tostring

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
        mainElement = Element("parserTreeHead")
        mainTree._setroot(mainElement)
        lm = ListManager.ListManager()
        lm.loadList(clearedList)
        
#        lm.parseListToElement()
#        tostring(mainElement)

        element = lm.parseListToElement()
        mainElement.append(element)
        
        f = open('file.xml', 'w')
        prettyXmlString = minidom.parseString(tostring(mainElement)).toprettyxml()
        f.write(prettyXmlString)
        
#        ElementTree(mainElement).write('file.xml')
if __name__ == '__main__':
    parser = Parser()
#    tList = ["", "a", "b", "","c","","q","abcde","tekst", "w"]
#    tList = ["", "a", "b", "","c","","'''","abcde","tekst", "'''"]
    tList = ["'''", "a", "1", "'''", "b", "'''", "c"]
    parser.loadTokenList(tList)
    parser.parse()
    
 