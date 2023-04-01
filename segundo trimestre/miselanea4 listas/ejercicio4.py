import random

a=[]
aux=[]
for i in range(random.randint(10,25)):
    a.append(random.randrange(100))
print(a)
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            aux,a[i]=a[i],a[j]
            a[j]=aux
print(a)
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]<a[j]:
            aux,a[i]=a[i],a[j]
            a[j]=aux
print(a)