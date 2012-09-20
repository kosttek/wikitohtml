# coding=UTF-8

from Tkinter import *
import ttk
from wikipack.parser import settings
from wikipack.scanner.ScannerPack import Scanner
from wikipack.parser.Parser import Parser



def parse(*args):
    try:
        
        wikitext = wikitext_entry.get("1.0", 'end')
        settings.loadWikiText(wikitext)
        options = settings.getOptions()
        
        scanner = Scanner()
        scanner.loadTree('data/wikitree2.xml')
        scanner.loadFile('parser/source/wikiSource.wiki')
        scanResult = scanner.scan()
        print scanResult

        parser = Parser()
        parser.loadTokenList(scanResult, options)
        parser.parse()
        
        htmltext = settings.loadHtmlText()
        print "htmltext"
        print htmltext
        htmltext_entry.delete("1.0", 'end')
        htmltext_entry.insert("1.0", htmltext)
#        try:
#            os.remove('pages/C.wiki')
#            os.remove('pages/C.html')
#        except:
#            None
    except ValueError:
        pass
    
root = Tk()
root.title("Wiki to Html")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

wikitext_entry = Text(mainframe, width=60, height = 40)
htmltext_entry = Text(mainframe, width=60, height = 40)

wikitext_entry.grid(column=1, row=2)
htmltext_entry.grid(column=3, row=2)

ttk.Button(mainframe, text="Konwertuj", command=parse).grid(column=2, row=1, sticky=N)
#
#ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
#ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
#ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()