num=1
cont2=0
while num<=1000:
    cont=1
    x=0
    while cont<=num:
        if num%cont==0:
            x+=1
        cont+=1
    if x==2:
        print(num)
        cont2+=1
    num=+1
print("Hay",cont2,"numeros primos")

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