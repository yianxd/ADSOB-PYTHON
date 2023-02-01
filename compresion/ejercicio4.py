import random
b=[int(random.randrange(100)) for i in range(random.randint(10,25))]
num=[(n,"es menor") if n!=0 and n<18  else (n,"es mayor de edad") for n in b ]
print(b,"\n",num)

"""
menor=[n for n in b if n!=0 and n<18]
mayor=[n for n in b if n>18]
print(menor,"\n",mayor)
"""