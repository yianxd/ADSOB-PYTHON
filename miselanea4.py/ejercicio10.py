import random 
a=[]
media,prom,suma=0,0,0
#prom=0
a1=[]
#suma=0
for i in range(random.randint(10,25)):
    a.append(random.randrange(100))
    prom+=a[i]
prom=prom/len(a)
print(a)
print(prom)
for i in range(len(a)):
    a1.append(a[i]-prom)
print(a1)
for i in range(len(a1)):
    a1[i]=a1[i]**2
    suma+=a1[i]

print("la desviacion estandar es: ",(suma/len(a)-1)**0.5)
