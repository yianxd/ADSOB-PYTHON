def num_primos():
    lista=[]
    con=0
    for i in range(101):
        cont=0
        for j in range(1,i):
            if i%j==0:
                cont+=1
        if cont==1:
            con+=1
            lista.append(i)
    return lista

def num_compuestos(num):
    lista=[]
    con=0
    for i in range(num):
        cont=0
        for j in range(1,i):
            if i%j==0:
                cont+=1
        if cont==1:
            con+=1
        else:
            lista.append(i)
    return lista

def num_fraccion(numerador,denominador):
    frac=(str(numerador)+"/"+str(denominador))
    return frac

def suma_fraccion(n1,d1,n2,d2):
    r=0
    if d1==d2:
        r=str(n1+n2)+"/"+str(d2)
        return r
    else:
        r=str(n1*d2+n2*d1)+"/"+str(d2*d1)
        return r
print(suma_fraccion(2,3,4,4))
def resta_fraccion(n1,d1,n2,d2):
    r=0
    if d1==d2:
        r=str(n1-n2)+"/"+str(d2)
        return r
    else:
        r=str(n1*d2-n2*d1)+"/"+str(d2*d1)
        return r
def multiplicacion_fraccion(n1,d1,n2,d2):
    r=str(n1*n2)+"/"+str(d2*d1)
    return r
def division_fraccion(n1,d1,n2,d2):
    r=str(n1*d2)+"/"+str(n2*d1)
    return r

