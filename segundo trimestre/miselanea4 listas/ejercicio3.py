import random
a=[]
par=0
for i in range(random.randint(10,25)):
    a.append(random.randrange(100))
for i in range(len(a)):
    if a[i]%2==0:
        print(a[i],"es par")
        par+=a[i]
print("el promedio de los pares es de: ",par/len(a))
        