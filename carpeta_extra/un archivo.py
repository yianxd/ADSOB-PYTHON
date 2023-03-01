import random 
n=random.randint(5,10)
a=[(i+1)**0.5 for i in range(n)]
print(a)

b=[int(random.randrange(100)) for i in range(random.randint(10,25))]

pares=[n for n in b if n%2==0]
impares=[n for n in b if n%2!=0]
#print(b,"\n",pares,"\n",impares)
pares2=[n if n%2==0 else "no es par" for n in b]
pares=tuple(pares)
print(pares)