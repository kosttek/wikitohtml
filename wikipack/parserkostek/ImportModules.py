'''
Created on 21-09-2012

@author: kosttek
'''
import os
import imp
MODULE_EXTENSIONS = ('.py',)

class ImportModules :
    modules = dict()
    parser = 0
       
    def __init__(self,parser) :
        for module in self.module_list():
            path = 'wikipack.parserkostek.parseModules.'+module+'.SpecialParse'
            object = self.my_import(path)
            if object == 0:
                continue 
            self.modules[module]=object()
        self.parser = parser
   
    def module_list(self):
        package_name = "parseModules"
        file, pathname, description = imp.find_module(package_name)
        if file:
            raise ImportError('Not a package: %r', package_name)
        # Use a set because some may be both source and compiled.
        return set([os.path.splitext(module)[0]
            for module in os.listdir(pathname)
            if module.endswith(MODULE_EXTENSIONS)])
    
    @staticmethod
    def my_import(name):
        components = name.split('.')
        path = ""
        for comp in components[:-1]:
            path+=(comp)+"."
        path = path[:-1]
        try:
            mod = __import__(path)
            for comp in components[1:]:
                mod = getattr(mod, comp)
        except AttributeError:
            return 0
        return mod
    
    def parse_special(self, moduleName):
        return self.modules[moduleName].parse(self.parser)

#print module_list()
#klass = my_import('wikipack.parserkostek.parseModules.modone.Mod_one')
#some_object = klass()
#some_object.func("moo")
if __name__ == '__main__':
    importM = ImportModules(0)
    #print importM.modules['break'].parse()
#    print importM.parse_special('break')
    print importM.modules
