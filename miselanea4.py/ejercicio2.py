import  random
a=[]
for i in range(random.randint(10,25)):
    a.append(random.randrange(100))

for i in a:
    cont=0
    for j in range(1,i):
        if i%j==0:
            cont+=1
    if cont==1:
        print(i)
