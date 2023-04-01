import random
a=[]
a1,a2=[],[]
a4,a5,a6=[],[],[]
m1,m2=0,0
t1,t2,t3=0,0,0
for i in range(30):
    a.append(random.randint(5,28))
a1=a[:15]
a2=a[15:31]
a4=a[0:10]
a5=a[10:20]
a6=a[20:31]
for i in range(len(a1)):
    m1+=a1[i]
    m2+=a2[i]
print("el promedio de la primera mitad es: ",m1/len(a1))
print("El promedio de la segunda mitad es: ",m2/len(a2))

for i in range(len(a4)):
    t1+=a4[i]
    t2+=a5[i]
    t3+=a5[i]
print("promedio del tercio 1 es: ",t1/len(a4))
print("promedio del tercio 2 es: ",t2/len(a5))
print("promedio del tercio 3 es: ",t3/len(a6))

a=[1.2 for i in range(3)]