import random 
a=[]
media,prom,suma=0,0,0
for i in range(random.randint(10,25)):
    a.append(random.randrange(100))
    prom+=a[i]
prom=prom/len(a)
for i in range(len(a)):
    a.append(a[i]-prom)
for i in range(len(a)):
    a[i]=a[i]**2
    suma+=a[i]
print("la desviacion estandar es: ",(suma/len(a)-1)**0.5)