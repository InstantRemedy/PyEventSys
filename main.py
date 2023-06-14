import sys

class Event:
    def __init__(self, *typeArgs) -> None:
        for tArg in typeArgs:
            if type(tArg) != type:
                print("Class event take in argument only type object")
                sys.exit()
        
        self.__typeArgs = typeArgs
        self.__events = []

    def addListener(self, fargs):
        self.__events.append(fargs)
    
    def removeListener(self, fargs):
        self.__events.remove(fargs)
    
    def invoke(self, *args):
        if len(args) != len(self.__typeArgs):
            print("Function have different count of args")
            sys.exit()
        
        for i in range(len(args)):
            if type(args[i]) != self.__typeArgs[i]:
                print("Function have other type of argument")
                sys.exit()
        
        
        for function in self.__events:
            function(*args)