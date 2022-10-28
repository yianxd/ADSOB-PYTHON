import random

x=random.randint(1,10)
n=0
cont=0

while n!=x:
    n=int(input("ingrese un numero:"))
    cont+=1
    if n>x:
        print(n,"es muy grande")
    if n<x:
        print(n,"es muy pequeño")
    if n==x:
        print("El numero es",n)
    print("intentos",cont)
        
           
