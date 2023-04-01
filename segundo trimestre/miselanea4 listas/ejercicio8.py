import random
a=[]
a2=[]
for i in range(random.randint(10,25)):
  a.append(random.randrange(100))
cont=0
for i in range(len(a)): 
    cont=0
    for j in a:    
        if a[i] == j:
            cont+=1 
    if cont!=0:
        a2.append(cont)
    else:
        a2.append(0)
print(a)
print(a2)
mayor=0
pos=0
for i in range(len(a)):
    if mayor<a2[i]:
       mayor=a2[i]
print('El mayor es ',mayor)
for j in range(len(a2)):
    if mayor==a2[j]:
        print('la moda es ',a[j])