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
    
    def loadTree(self, path):
        self.tree = ElementTree()
        self.tree.parse(path)
    
    def loadFile(self, path):
        self.file = open(path, 'r')
        
    
        
    def scan(self):
        treeElement = self.tree.getroot()
        for line in self.file.readlines() : 
            lineMark = self.checkLineStartEndMarks(line)
            token_list = self.scanLine(lineMark[0] )
            token_list.append(lineMark[1])
            token_list.append("\n")
            token_list.insert(0,lineMark[1])
            token_list.insert(0,lineMark[2])
            print token_list
            
            print "---------------------------"
            
    def scanLine(self, line):
        #class Namespace: pass
        
        def setEndMark(vo):
            #print "return - >",vo.retMark
            ret.append(vo.tempString)
            vo.tempString = ""
            ret.append(vo.markAcumulator) # ret.append(vo.retMark)
            vo.markAcumulator = ""
            vo.treeElement = vo.root
            vo.retMark = 0
            
        class varObject:
            #TODO sprobowac z find
            treeElement = self.tree.getroot().iter("chars").next() 
            root = treeElement
            retMark = 0
            
        ret = list()
        vo = varObject()
        vo.tempString = ""
        vo.markAcumulator = ""
        
        for character in line:
            
            for element in list(vo.treeElement):
                
                if element.attrib["value"] == character:
                    vo.markAcumulator +=  character
                    vo.retMark = element.get("return", 0)
                    if len(list(element)) == 0:
                        setEndMark(vo) 
                    else:
                        vo.treeElement = element
                    break
                elif vo.retMark != 0:
                    setEndMark(vo)
                    break
                else:
                    vo.tempString += vo.markAcumulator + character
                    vo.markAcumulator = ""
                    vo.treeElement = vo.root
                    vo.retMark = 0 
                    
        ret.append(vo.tempString)
        
        return ret            

                    
            
            
    def checkLineStartEndMarks(self, line):
        '''Minimal length of firstmark and linemark is not implemented. It seems to be not obligatory now
        '''
        return_mark = ""
        return_first_mark = ""
        start_i_value = 0
        
        if line[-1]=='\n':
            endcount = -1
        else:
            endcount =  0
        
        if len(line) > 2:
            treeElement = self.tree.getroot()
            
            for element in treeElement.iter("firstmark"):
                if element.attrib['value'] == line[0]:
                    firstmark = element.attrib['value']
                    while line[start_i_value] == firstmark:
                        start_i_value+=1
                        return_first_mark+=firstmark
                
            for element in treeElement.iter("linemark"): 
                if element.attrib['value'] == line[start_i_value] and element.attrib['value'] == line[-2]:
                    mark = element.attrib['value']
                    for i in range(0, int(element.attrib['max'])):
                        if mark == line[i+start_i_value] and mark == line[-1 - i + endcount]:
                            return_mark+=mark;
                        else:
                            return (line[i+start_i_value:endcount-i] , return_mark, return_first_mark)
        return (line[start_i_value:endcount] , return_mark , return_first_mark)
    
    
    
    
if __name__ == '__main__':
    scanner = Scanner()
    scanner.loadTree('../data/wikitree2.xml')
    scanner.loadFile('../data/testfile')
    scanner.scan()
