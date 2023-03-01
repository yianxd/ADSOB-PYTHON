x=10 #se determina una variable
x=[] #se le cambia el valor a la variable x
cad='amo la programación' #se determina la variable 
print(type(cad)) #permite ver el tipo de dato
print(len(cad)) #muestra por pantalla el len de la variable(cad)
print(cad.capitalize()) #pone la primera letra en mayus


class Persona: #inicio dela clase
    def __init__(self,nombre): #inicializa el contructor con un def __init__ y dentro del parentesis un "self" y despues los atributos
        self.__nombre=nombre #define los arributos
        print('Activando constructor') #mensaje que se siempre se va a ejecutar cuando se inicialice un objeto

    def getNombre(self): #metodo get que permite visualizar los atributos asi esten privados
        return self.__nombre #returna el atributo "nombre"
    
    def setNombre(self, nombre): #metodo set que permite cambiar un atributo
        self.__nombre=nombre

    def metodo(self): #es un motodo de la clase "persona"
        print('Soy un método') #mensaje que ejecuta


ob=Persona('Ana') #se crea un objeto de la clase persona y se le da como atributo "Ana"
print(ob.getNombre()) #imprime por pantalla el objeto creado y gracias al getNombre se podra ver el atributo
ob.setNombre('Maria') #el metodo .setNombre envia el un parametro con que el se va a cambiar un atributo 
print(ob.getNombre()) #imprime por pantalla el objeto creado y gracias al getaNombre se podra ver el atributo
#ob.metodo() / se llama el metodo 
#print(type(ob)) #muestra el tipo de dato que es "ob"