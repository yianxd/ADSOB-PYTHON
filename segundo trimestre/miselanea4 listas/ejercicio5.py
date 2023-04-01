import random
a=[]
con=0
num=int(input())
for i in range(random.randint(10,25)):
    a.append(random.randrange(100))
for i in range(len(a)):
    if len(a)==i:
        con+=1
    else:
        continue
if num not in a:
    a.append(num)
print("el numero esta: ",con)
print("la lista se a acutalizado",a)