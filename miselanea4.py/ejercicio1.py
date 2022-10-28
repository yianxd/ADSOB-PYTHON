import random
""""
1)llenar una lista de tamaño aleatorio entre 10 y 25 elementos.
2)llene la lista con numeros aleatorios.
3)De cada elemento de la lista diga si el elemento esta por encima del promedio,debajo o es igual al promedio de todos los numeros de la lista
"""
"""
num=int(input("Ingrese un valor entre 10 y 25: "))
while num<10 or  num>25:
    num=int(input("Ingrese un valor entre 10 y 25: "))
"""
a=[]
promedio=0
count=0
for i in range(random.randint(10,25)):
    count+=1
    a.append(random.randrange(100))
    promedio+=a[i]
promedio=promedio//len(a)
print("el promedio es",promedio)
for i in range(len(a)):
    if a[i]==promedio:
        print(a[i],"el valor es igual al promedio")
    elif a[i]<promedio:
        print(a[i],"es menor al promedio")
    else:
        print(a[i],"es mayor al promedio")