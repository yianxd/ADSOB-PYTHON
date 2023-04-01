import random
b=[int(random.randrange(100)) for i in range(10)]
num=[n if n<=9 else 0 for n in b ]

print(b,"\n",num)