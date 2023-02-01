con=0
for i in range(1001):
    cont=0
    for j in range(1,i):
        if i%j==0:
            cont+=1
    if cont==1:
        print(i)
        con+=1

print("Hay",con,"numeros primos")

"""
numero=1
while numero <=100:
    contador=1
    x=0
    while contador<=numero:
        if numero%contador==0:
            x+=1
            contador = contador +1
    if x==2:
        print(numero)
    numero+=1
"""
""""

"""