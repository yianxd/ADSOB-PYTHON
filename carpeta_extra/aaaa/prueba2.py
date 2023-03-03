class Carro:
    def arrancar(self):
        print("...")
        
class bus(Carro):
    def arrancar(self):
        print("El bus arranco a x km/h")
        

#ob1=Carro()
#ob2=bus()

#ob1.arrancar()
#ob2.arrancar()

class ser_vivo:
    def hablar(self):
        print("un ser vivo emite un ruido para comunicarse")
        
class persona(ser_vivo):
    def hablar(self):
        print("La persona habla un idioma")
        
class perro(ser_vivo):
    def hablar(self):
        print("el perro ahulla")
        
obj3=ser_vivo()        
obj1=perro()
obj2=persona()

print(obj1.hablar(),obj2.hablar(),obj3.hablar(),end=" ")