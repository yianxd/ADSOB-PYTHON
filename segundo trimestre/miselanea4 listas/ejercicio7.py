import random 
a=[]
suma=0
for i in range(random.randint(10,25)):
    a.append(random.randrange(100))
    suma+=a[i]
print(suma)
print(suma/len(a))