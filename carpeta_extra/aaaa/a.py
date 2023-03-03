class Empleado:
    c=0
    def __init__(self,nombre,cargo,salario,h_extra):
        self.__nombre = nombre
        self.__cargo = cargo
        self.__salario = salario
        self.__h_extra=h_extra
        self.__class__.c+=1
        print(self.c)
    #----------------------------------------------------------------    
    def getNombre(self):
        return self.__nombre
    def getCargo(self):
        return self.__cargo
    def getSalario(self):
        return self.__salario
    #----------------------------------------------------------------
    def setNombre(self,nombre):
        self.__nombre = nombre
        
    def setCargo(self,cargo):
        self.__cargo = cargo
        
    def setSalario(self,salario):
        self.__salario = salario
    #----------------------------------------------------------------
    def calcular(self):
        self.__horas = (self.__salario/30)/8
        return self.__horas
    
    def ipc(self):
        if  self.__salario==1300000:
            self.__aumento=(self.__salario*0.16)+self.__salario
            return self.__aumento
        elif self.__salario>13000000:
            self.__aumento2=(self.__salario*0.13)+self._salario
            return self.aumento2
        
    def horas_Extra(self):
        if self.__h_extra<=2:
            self.__salario_extra = (self.__h_extra*self.__horas)+self.__salario
            return self.__salario_extra
        else:
            print("error")
        


ob1=Empleado("Juan","aaaaaa",1400000,2)
ob2=Empleado("elian","asasa",1300000,2)
ob1.ipc()
ob1.calcular()
print(ob1.ipc())
print(ob1.__dict__)