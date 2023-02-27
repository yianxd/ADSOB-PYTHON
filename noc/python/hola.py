import math

def formula_cuadratica(a,b,c):
    try:
        x_positiva=(-b+math.sqrt(b**2-4*a*c))/(2*a)
        x_negativa=(-b-math.sqrt(b**2-4*a*c))/(2*a)
        print(x_negativa,x_positiva) 
    except ZeroDivisionError:
        print("No se puede dividor por cero")
    except ValueError:
        print("xd")
    except TypeError:
        print("No recibe otro valor que no sea numero")

formula_cuadratica("a","a","a")

def semana(dia):
    try:
        sem=["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
        print(sem[dia])
    except IndexError:
        print("no existe ese dia de la semana")
    except TypeError:
        print("que poronga es eso?")
semana({})

blog_posts = [{'Photos': 3, 'Megusta': 21, 'comentarios': 2}, {'Megusta': 13, 'comentarios': 2, 'compartido': 1}, {'Photos': 5, 'Megusta': 33, 'comentarios': 8, 'compartido': 3}, {'comentarios': 4, 'compartido': 2}, {'Photos': 8, 'comentarios': 1, 'compartido': 1}, {'Photos': 3, 'Megusta': 19, 'comentarios': 3}]

total_Megusta = 0
try:
    for post in blog_posts:
        total_Megusta = total_Megusta + post[1][1]
    print(total_Megusta)
except KeyError:
    print("xd")

print(total_Megusta)
    