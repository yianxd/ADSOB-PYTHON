class Usuarios:
    num_u=0
    def __init__(self,id,name,age,brithDay,contactnum,password):
        self.__class__.num_u+=1
        self.id = id
        self.name = name
        self.age = age
        self.brithDay = brithDay
        self.contactnum = contactnum
        self.__password = password
        
    def getPassword(self):
        return self.__password
    
    def actualizarAge(self,NewName):
        self.name = NewName
    
    def actualizarNum(self,NewNum):
            self.contactnum = NewNum
    
    def actualizarName(self,NewAge):
            self.name = NewAge
            
    def actualizarName(self,NewName):
            self.__name = NewName

class Instructors(Usuarios):
    num_ins=0
    def __init__(self,id,name,contactnum,password,credentials):
        Usuarios().__init__(self,id,name,contactnum,password)
        self.__class_.num_u+=1
        self.courser=[]
        self.credentials = credentials
        self.__username="instructorN" #buscar manera de usar la variable de clase para generar el usuario
        print("")
        
    def verCredenciales(self):
        return self.__username, self.__password
    
class Students(Usuarios):
    num_st=0
    def __init__(self,id,name,contactnum,username,password):
        self.couser = []
        self.__class__.num_st+=1
        Usuarios().__init__(self,id,name,contactnum,username,password)
        self.__username="EstudianteN" #buscar la manera de usar la variable de clase para generar el usuario
    
    def verCredenciales(self):
        return self.__username,self.__password
    
    def EliminarCursos(self,curso): 
        if curso in self.couser:
            self.couser.remove(curso)
            return self.couser

        
class Trasactions:
    def __init__(self,id,datails,date):
        self.id = id
        self.datails = datails
        self.date = date
        
    def processDebit(self):
        pass 


class Subjects:
    def __init__(self,id,name,description,schedule):
        self.id = id
        self.name = name
        self.description = description
        self.instructor=[]
        self.schedule=schedule
        
class Course:
    def __init__(self,id,description,date,yearlevel):
        self.id=id
        self.canestudiante=[]
        self.description=description
        self.date=date
        self.yearlevel=yearlevel
        

class Enrollment:
    def __init__(self,id,details,requirements,date):
        self.id=id
        self.details=details
        self.requirements=requirements
        self.date=date