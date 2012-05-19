import ListManager

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
        

if __name__ == '__main__':
    parser = Parser()
    tList = ["", "a", "b", "","c",""]
    parser.loadTokenList(tList)
    parser.parse()
    
 