class Curso:
    def __init__(self,titulo):
        self.__titulo=titulo

    def getTitulo(self):
        return self.__titulo

class Aprendiz:
    def __init__(self,nombre):
        self.__nombre=nombre
        self.__cursos=[]

    def agregarCurso(self,nombreCursito):
        cursito=Curso(nombreCursito)
        self.__cursos.append(cursito)

    def getCursos(self):
        return self.__cursos
    
ap=Aprendiz('Sofia')
ap.agregarCurso('Python Basico')
ap.agregarCurso('Python Intermedio')

for c in ap.getCursos():
    print(c.getTitulo())
    
#----------------------------------------------------------------    

class Aprendiz:
    def __init__(self,nombre):
        self.__nombre=nombre
        self.__cursos=[]

    def agregarCurso(self,titulo):
        self.__cursos.append(titulo)

    def getCursos(self):
        return self.__cursos

class Curso:
    def __init__(self,titulo):
        self.__titulo=titulo

    def getTitulo(self):
        return self.__titulo
    
a=Aprendiz('Martha')
c1=Curso('Python Intermedio')
c2=Curso('Python Basico')
c3=Curso('Introduccion a Java')

a.agregarCurso(c1)
a.agregarCurso(c2)
a.agregarCurso(c3)

print(a.getCursos())


for curso in a.getCursos():
    print(curso.getTitulo())
    
#------------------------------------------------------------------------------------------------------
#Version 1
def suma (a,b): #la funcion inicia aqui y pide 2 parametros
    return a+b #retorna una suma

def suma(a,b,c): #la funcion inicia aqui y pide 3 parametros
    return a+b+c #retorna una suma

print(suma(1,2,3)) #imprime la funcion la funcion suma y no dara error

#Version 2
def suma (a,b,c): #la funcion inicia aqui y pide 3 parametros
    return a+b+c #retorna una suma

def suma(a,b): #la funcion inicia aqui y pide 2 parametros
    return a+b #retorna una suma

print(suma(1,2,3)) #dara error porque python es un lenguaje interpretado al ejecutar linea por linea la 2da funcion suma reemplaza a la primera

#-------------------------------------------------------------------------------------------------------
class A1: #inicio de la clase A1
    def __init__(self): #inicializa el constructor
        pass #deja el constructor vacio
    def saludo(self):
        print('Hola desde A1')

class A2:
    def __init__(self):
        pass
    def saludo(self):
        print('Hola desde A2')


class B(A2,A1):
    def __init__(self):
        pass
    def saludo(self):
        print('Hola desde B')
    def __str__(self):
        return 'Soy un objeto de la clase B'
obj=B()
print(obj.__str__())
#obj.saludo()
#obj.saludo()


# cad="sena"
# lista=[1,2,3]
# print(cad.__str__())
# print(lista.__str__())