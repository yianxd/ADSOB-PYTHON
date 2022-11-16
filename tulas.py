import random
b=tuple(int(random.randrange(100)) for i in range(random.randint(10,25)))
for i in b:
    cont=0
    for j in range(1,i):
        if i%j==0:
            cont+=1
    if cont==1:
        print(i)

#print("la cantidad de primos es",count1)
print(b)


