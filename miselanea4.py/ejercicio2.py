import  random
from sqlite3 import connect
"""
1)llenar una lista de tamaño aleatorio entre 10 y 25 elementos.
2)llene la lista con numeros aleatorios.
3).Muestre cuales y cuantos son primos
"""
a=[]
suma1=0
count1=0
count=0
for i in range(random.randint(10,25)):
    a.append(random.randrange(100))

for i in range(len(a)):
    if a[i]%2==20:
        count+=1
    if count>2:
        continue
    else:
        print(a[1],"el numero es primo")
        count1+=1
        suma1=suma1+a[i]
print("la cantidad de primos es",count1)
print(a)
