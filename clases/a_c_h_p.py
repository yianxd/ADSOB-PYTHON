#----ඞ---


class Curso: #Inicio de la clase curso
    def __init__(self,titulo): #inicializa el constructor con un atributo
        self.__titulo=titulo #contructor del tributo "titulo"

    def getTitulo(self): #metodo get de titulo
        return self.__titulo # retorna "titulo"

class Aprendiz: #inicio de la clase aprendiz
    def __init__(self,nombre): #inicializa el constructor con un atributo
        self.__nombre=nombre #contructor del nombre
        self.__cursos=[] #se crea un atributo cursos(una lista) en la clase

    def agregarCurso(self,nombreCursito): #inicio del metodo agregarCurso que toma un atributo
        cursito=Curso(nombreCursito) #en la variable cursito utilizando la clase Cursos 
        self.__cursos.append(cursito) #agregar  en el atributo del constructor "curso" el atributo "cursito" 

    def getCursos(self): #inicio del metodo get de cursos
        return self.__cursos #retorna cursos
    
ap=Aprendiz('Sofia') #crea un objeto de la clase aprendiz
ap.agregarCurso('Python Basico') #crea un objeto curso 
ap.agregarCurso('Python Intermedio')#crea un objeto curso

for c in ap.getCursos(): #inicia un for con la variable curso que recorre la clase ap
    print(c.getTitulo()) #imprime el contenido en cada ciclo
    
#----------------------------------------------------------------     ඞ

class Aprendiz: #inicio de la clase aprendiz
    def __init__(self,nombre): #inicializa el constructor con un paramatro
        self.__nombre=nombre #contructor del atributo nombre
        self.__cursos=[] #crea el atributo cursos en la clase

    def agregarCurso(self,titulo): #inicia el metodo agregarCurso con un paramatro
        self.__cursos.append(titulo) #agrega en el atributo cursos "titulos"

    def getCursos(self): #metodo get de cursos
        return self.__cursos #retorna cursos

class Curso: #incio de la clase cursos
    def __init__(self,titulo): #inicializa el constructor con un atributo
        self.__titulo=titulo #constructor del atributo titulo

    def getTitulo(self): #get de titulo
        return self.__titulo #retorna titulo
    
a=Aprendiz('Martha') #crea un objeto de la clase aprendiz
c1=Curso('Python Intermedio') #crea un objeto de la clase curso
c2=Curso('Python Basico') #crea un objeto de la clase curso
c3=Curso('Introduccion a Java') #crea un objeto de la clase curso

a.agregarCurso(c1) # con la clase a del objeto aprendiz se llama el metodo agregar cursos
a.agregarCurso(c2) # se le envia como parametro un objeto de la clase curso
a.agregarCurso(c3) # se repite 3 veces

print(a.getCursos()) #imprime cursos 


for curso in a.getCursos(): #un for que recorre el contenido del objeto a unicamente con el metodo getCursos
    print(curso.getTitulo()) #imprime la variable cursos con  el metodo getTitulo
    
#------------------------------------------------------------------------------------------------------
#Version 1
def suma (a,b): #la funcion inicia aqui y pide 2 parametros
    return a+b #retorna una suma

def suma(a,b,c): #la funcion inicia aqui y pide 3 parametros
    return a+b+c #retorna una suma

print(suma(1,2,3)) #imprime la funcion suma y no dara error

#Version 2
def suma (a,b,c): #la funcion inicia aqui y pide 3 parametros
    return a+b+c #retorna una suma de 3 variables

def suma(a,b): #la funcion inicia aqui y pide 2 parametros
    return a+b #retorna una suma 2 variables

print(suma(1,2,3)) #dara error porque python es un lenguaje interpretado al ejecutar linea por linea la 2da funcion suma reemplaza a la primera

#-------------------------------------------------------------------------------------------------------
class A1: #inicio de la clase A1
    def __init__(self): #inicializa el constructor
        pass #deja el constructor vacio
    def saludo(self): #inicio de un metodo
        print('Hola desde A1') #imprime por pantalla el mensaje

class A2: #inicio de la clase A2
    def __init__(self): #inicializa el constructor 
        pass #deja el constructor vacio
    def saludo(self): #inicio de un metodo
        print('Hola desde A2') #imprime por pantalla el mensaje


class B(A2,A1): #inicio de la clase B que hereda los metodos de "A" y "A1"
    def __init__(self): #inicializa el constructor 
        pass #deja el constructor vacio 
    def saludo(self): #inicio de un metodo
        print('Hola desde B') #imprime por pantalla el mensaje
    def __str__(self): #no me acuerdo que hacia el __str__ ;-;
        return 'Soy un objeto de la clase B' #retorna el mensaje
obj=B() #se crea un objeto de la clase B
print(obj.__str__())
#obj.saludo()
#obj.saludo()
# :]

# cad="sena"
# lista=[1,2,3]
# print(cad.__str__())
# print(lista.__str__())