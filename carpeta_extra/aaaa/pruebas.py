class Super:
    var=0
    def __init__(self,nombre,numero):
        self.nombre = nombre
        self.numero = numero
        
    def imprimir(self):
        return self.nombre
    
    def numer(self):
        var= self.numero + 1
        return var
    
class SuperB:
    def __init__(self,nombre,decimal):
        self.nombre = nombre
        self.decimal = decimal
        
    def crear(self):
        return self.nombre+":)"
    
    
    
class Sub(Super,SuperB):
    var=20
    def __init__(self,nombre,numero,decimal):
        Super.__init__(self,nombre,numero)
        SuperB.__init__(self,nombre,decimal)
    
    
class Sub2(Sub):
    def __init__(self,nombre,numero,decimal):
        Sub.__init__(self,nombre,numero,decimal)
        
        
ob=Sub("a",1,1.2)
print(ob.__dict__)
print(ob.imprimir())
print(ob.numer())
print(ob.var)
print(ob.crear())

ob2=Sub2("b",2,2.2)
print(ob2.__dict__)
