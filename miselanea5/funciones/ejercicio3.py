import random
#generar listas random y asi
def lista_random(lista):
    lista=[]
    for i in range(random.randint(10,25)):
        lista.append(random.randrange(100))
    return lista
#ejercicio 1 listas
#ejercicio 9 prom==mediana
def prom_listas(lista):
    prom=0
    for i in lista:
        prom+=i
    prom=prom/len(lista)
    return prom

def mayor_menos_prom(lista):
    prom=prom_listas(lista)
    for i in range(len(lista)):
        if lista[i]==prom:
            print(lista[i],"el valor es igual al promedio")
        elif lista[i]<prom:
            print(lista[i],"es menor al promedio")
        else:
            print(lista[i],"es mayor al promedio")
#ejercicio 3 listas
def par_listas(lista):
    par=[]
    for i in range(len(lista)):
        if lista[i]%2==0:
            par.append(lista[i])
            print(lista[i],"es par")
    return par
#ejercicio 5 lista
def agregar_lista(lista,num):
    con=0
    for i in lista:
        if num!=i:
            continue
        else:
            con+=1
    if num not in lista:
        lista.append(num)
    print("el numero estaba",con)
    return lista
#ejercicio 10
def desviacion(lista):
    lista2=[]
    prom=prom_listas(lista)
    suma=0
    for i in range(len(lista)):
        lista2.append(lista[i]-prom)
        lista2[i]=lista2[i]**2
        suma+=lista2[i]
    desviacion=((suma**0.5)/len(lista)-1)**0.5
    return desviacion
#ejercicio 6
def finabonacci(num):
    lista=[0,1]
    if num>5 and num<20:
        for i in range(num):
            lista.append(lista[-1]+lista[-2])
    return lista
#ejercicio 8
def moda(lista):
    lista2=[]
    cont=0
    mayor=0
    pos=0
    moda=0
    for i in range(len(lista)): 
        cont=0
        for j in lista:    
            if lista[i] == j:
                cont+=1 
        if cont!=0:
            lista2.append(cont)
        else:
            lista2.append(0)
    for i in range(len(a)):
        if mayor<lista2[i]:
            mayor=lista2[i]
        for j in range(len(lista2)):
            if mayor==lista2[j]:
                moda=lista[j]
    return moda
