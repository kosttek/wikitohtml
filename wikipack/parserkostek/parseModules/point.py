'''
Created on 21-09-2012

@author: kosttek
'''
from xml.dom.minidom import Document
from wikipack.parserkostek.parserBegining import Parser

class SpecialParse:
    sign = '#'
    inc_count = 0
    lines = []
    parser = Parser()
    
    def parse(self,parser):
        self.makeLines(parser)
        return [self.parsePoints(self.lines),self.inc_count]
    
    def parsePoints(self,lines):
        parent = Document().createElement("ol")
        self.delFirstLineChar(lines)
        node = 0
        newTab = []
        if lines[0][0] != '':
            node = Document().createElement("li")
        for line in lines:
            if line[0] == '':
                if node != 0 :
                    self.appendNode(node, newTab)
                    newTab = []
                    parent.appendChild(node)
                node = Document().createElement("li")
                nodes = self.parseTextLine(line[1:])
                for smallnode in nodes[:]:
                    node.appendChild(smallnode)
            else :
                newTab.append(line)
        self.appendNode(node, newTab)        
        parent.appendChild(node)
        return parent
                
    def appendNode(self,node,newTab):
        if len(newTab) == 0:
            return 
        node.appendChild(self.parsePoints(newTab))
        
    def parseTextLine(self,line):
        self.parser.setTokenList(line)
        self.parser.count = 0
        retNode = self.parser.parseToken("*container", None)
        childs = retNode.childNodes
        return childs
        
        
    
    def makeLines(self,parser):
        self.lines = []
        lines = self.lines
        count = parser.count - 1
        while parser.tokenList[count][0]==self.sign:
            line = []      
            while True:
                token = parser.tokenList[count]
                line.append(token)
                count+=1
                if  token == '\n' :
                    break
            lines.append(line)
        self.inc_count = count - (parser.count -1)
        print self.inc_count
        print lines
        
    def delFirstLineChar(self,lines):
        for line in lines :
            line[0] = line[0][1:]
    