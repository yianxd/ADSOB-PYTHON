class empresa:
    def __init__(self,index,oId,name,website,country,description,founded,industry,numE):
        self.__index=index
        self.__oId=oId
        self.__name=name
        self.__website=website
        self.__country=country
        self._description=description
        self.__founded=founded
        self.__industry=industry
        self.__numE=numE

    def verTodo(self):
        return self.__index+" "+self.__oId+" "+self.__name+" "+self.__website+" "+self.__country+" "+self.__founded+" "+self.__industry+" "+self.__numE
    
    def getFounded(self):
        return self.__founded
    
    def getName(self):
        return self.__name