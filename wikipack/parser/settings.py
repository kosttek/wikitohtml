import os

srcFilename = 'wikiSource'
filePath = os.path.normpath(  os.path.join( os.path.dirname(__file__), 'source'))

    
def loadWikiText(wikitext):
    text_file = open(filePath +'/' +srcFilename + '.wiki', "w")
    text_file.write(wikitext)
    text_file.close()
    
def getOptions():
    options = Setting()
    options.srcdir = filePath
    options.destdir = filePath
    options.all = True
    
    return options

def loadHtmlText():
    text_file = open(filePath +'/' +srcFilename + '.html', "r")
    htmltext = text_file.read()
    text_file.close()
    os.remove(filePath +'/' +srcFilename + '.html')
    os.remove(filePath +'/' +srcFilename + '.wiki')
    return htmltext

class Setting(object):
    srcdir = None
    destdir = None
    all = False
    
    