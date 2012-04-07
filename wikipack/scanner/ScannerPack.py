'''
Created on 07-04-2012

@author: kosttek
'''

import sys
from xml.etree.ElementTree import ElementTree


class Scanner:
    tree = 0
    file = 0
    treeElement = 0
    
    def loadTree(self,path):
        self.tree = ElementTree()
        self.tree.parse(path)
    
    def loadFile(self,path):
        self.file = open(path,'r')
        
    
        
    def scan(self):
        treeElement = self.tree.getroot()
        for line in self.file.readlines() : 
            lineMark =  self.checkLineStartEndMarks(line)
            self.scanLine(line)
            print "---------------------------"
            
    def scanLine(self,line):
        ret = list()
        
        def setEndMark(vo):
            print "return - >",vo.retMark
            vo.treeElement = vo.root
            vo.retMark =0
        
        class varObject:
            #TODO sprobowac z find
            treeElement = self.tree.getroot().iter("chars").next() 
            root = treeElement
            retMark = 0
            
        vo = varObject()
        for character in line:
            
            for element in list(vo.treeElement):
                
                if element.attrib["value"]==character:
                    
                    vo.retMark = element.get("return",0)
                    if len(list(element)) == 0:
                        setEndMark(vo) 
                    else:
                        vo.treeElement = element
                    break
                elif vo.retMark != 0:
                    setEndMark(vo)
                    break
                else:
                    vo.treeElement = vo.root
                    vo.retMark =0 
                    
                    

                    
            
            
    def checkLineStartEndMarks(self,line):
        if len(line)>2:
            treeElement = self.tree.getroot()
            for element in treeElement.iter("linemark"): 
                if element.attrib['value'] == line[0] and element.attrib['value'] == line[-2]:
                    mark = element.attrib['value']
                    for i in range(1,int(element.attrib['max'])):
                        if mark == line[i] and mark == line[-2-i]:
                            pass
                        else:
                            return {i, mark}
        return {0,""}
    
if __name__ == '__main__':
    scanner = Scanner()
    scanner.loadTree('../data/wikitree2.xml')
    scanner.loadFile('../data/testfile')
    scanner.scan()