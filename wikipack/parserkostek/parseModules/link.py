'''
Created on 21-09-2012

@author: kosttek
'''
from xml.dom.minidom import Document
from wikipack.parserkostek.parserBegining import Parser

class SpecialParse:
    inc_count = 0
    new_parser = Parser()
    link_content = 0
    
    def parse(self,parser):
        self.scanForClosing(parser)
        return [self.createLinkElement(),self.inc_count]
        
    def scanForClosing(self,parser):
        temp_count = parser.count
        while True:
            token = parser.tokenList[temp_count]
            if token == ']]' or temp_count > len(parser.tokenList)-1:
                break
            temp_count += 1
        self.inc_count = temp_count - parser.count+2
        self.link_content = parser.tokenList[parser.count:temp_count]
        
    def createLinkElement(self):
        a = Document().createElement("a")
        text = ''
        http = self.link_content[0]
        if len(self.link_content) == 1:
            text =  Document().createTextNode(http)
            a.appendChild(text)
        else:
            in_count = 1
            if(self.link_content[1]=='|'):
                in_count = 2
            self.new_parser.tokenList = self.link_content[in_count:]
            self.new_parser.count = 0
            container = self.new_parser.parseToken("*container",'')
            nodes = container.childNodes
            for smallnode in nodes[:]:
                a.appendChild(smallnode)
        a.setAttribute("href", http)
        return a
            
    