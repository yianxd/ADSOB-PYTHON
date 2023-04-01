#ejercicio 1 condicionales
def num_medio(n1,n2,n3):
    if n1>n2:
        if n1<n3:
            print("n1 es el numero del medio",n1)
        elif n3>n2:
            print("n3 es el numero del medio",n3)
    elif n1>n2:
        print("n2 es el numero del medio", n2)
    elif n2<n3:
        print("n2 es el numero del medio", n2)
    elif n3<n2:
        if n1<n2:
            print("n1 es el numero del medio", n1)
    elif n2>n3:
        print("n3 es el numero del medio",n3)
    else:
        print("n1 es el numero del medio", n1)
#ejercico 2 condicionales
def valores_iguales(n1,n2,n3):
    if n1==n2==n3:
        print("todos son iguales")
    elif n1==n2:
        print("el primero y segundo son iguales")
    elif n1==n3:
        print("el primer valor y tercero son iguales")
    elif n2==n3:
        print("el segundo y tercero son iguales")
    else:
        print("no son iguales")
#ejercicio 4 condicionales
def nota(nota):
    if nota<=5:
        print("Insuficiente")
    elif nota>4 and nota<7:
        print("suficiente")
    else:
        print("Bien")

#ejercicio 14 condicionales
def vueltas(angulo):
    a=1
    pi=3.1415
    if angulo<=360:
        print("a dado",a,"vuelta")
        print("la medida en radianes es:",angulo*pi/180)
    else:
        a=a+(angulo//360)
        print("a dado",a,"vuelta")
        print("la medida en radianes es:",angulo*pi/180)

#ejercicio 8
def coste_llamada(minutos):
    if minutos<=3:
        print("el coste es de: ", minutos*200)
    else:
        print("el coste es de: ",(50*(minutos-3))+600)
coste_llamada(3)