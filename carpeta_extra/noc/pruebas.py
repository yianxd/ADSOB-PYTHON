""""
class Clase1:
    num_u=0
    def __init__(self,contraseña):
        self.__class__.num_u+=1
        self.__contraseña=contraseña
        
    
        
class Clase2(Clase1):
    num_ins=0
    def __init__(self,contraseña):
        Clase1.__init__(self,contraseña)
        self.__class__.num_ins+=1
        self.__username="usuario"
        self.__contraseña=contraseña
        
    def verCredenciales(self):
        return self.__username,self.__contraseña
        
        
ob1=Clase2("dfghjkl")


print(ob1.num_u)
print(ob1.verCredenciales())


curso=["A","b","c","d","e","f","g","h","i"]

a=input()
if a in curso:
    curso.remove(a)
    print("Se a actualizado correctamente",curso)

----------------------------------------------
class Cursos:
    def __init__(self,nombre):
        self.nombre=nombre
        

class Clase1:
    def __init__(self):
        self.cursos=[]
        

"""


class Persona:
    def __init__(self,num):
        self.__num=num
        
    def getNum(self):
       return self.__num
   
    def setNum(self,numNew):
        self.__num=numNew
     
     
ob1=Persona(1)
print(ob1.getNum())
print(ob1.setNum(2))
print(ob1.getNum())