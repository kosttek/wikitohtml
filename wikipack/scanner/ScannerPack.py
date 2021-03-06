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
        result_list = list();
        for line in self.file.readlines() : 
            lineMark = self.checkLineStartEndMarks(line)
            token_list = self.scanLine(lineMark[0] )
            token_list.append(lineMark[1])
            token_list.append("\n")
            token_list.insert(0,lineMark[1])
            token_list.insert(0,lineMark[2])
            result_list.extend(token_list)

            

        self.file.close()
        return result_list
            
    def scanLine(self, line):
        #class Namespace: pass
        
        def setEndMark(vo):
            #print "return - >",vo.retMark
            if vo.tempString != "":
                ret.append(vo.tempString)
            vo.tempString = ""
            ret.append(vo.markAcumulator) # ret.append(vo.retMark)
            vo.markAcumulator = ""
            vo.treeElement = vo.root
            vo.retMark = 0
            vo.added = 1
        class VarObject:
            #TODO sprobowac z find
            treeElement = self.tree.getroot().iter("chars").next() 
            root = treeElement
            retMark = 0
            added = 0
            tempString = ""
            markAcumulator = ""
            
        ret = list()
        vo = VarObject()
        
        for character in line:
            elemetns_list = list(vo.treeElement)
            for element in elemetns_list:
                
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
                    vo.tempString += character
                    break
                elif vo.treeElement != vo.root:
#                    print elemetns_list.index(element ), element.attrib, len(elemetns_list)
                    if elemetns_list.index(element ) < len(elemetns_list)-1:
                        pass
                    else:
                        vo.tempString += vo.markAcumulator
                        vo.markAcumulator = ""
                        vo.treeElement = vo.root
                        vo.retMark = 0
                else:
                    pass
            
            if vo.added == 1:
                vo.added=0
            elif vo.treeElement == vo.root:
                vo.tempString +=  character +vo.markAcumulator
            
                     
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
            endcount =  len(line)
        
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
    result = scanner.scan()
    print result
