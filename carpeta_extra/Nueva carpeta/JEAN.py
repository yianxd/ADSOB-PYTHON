def log(base,n):
    c=1
    n2=base
    while n2<n:
        if n2!=n:
            n2*=base
            c+=1
    return c

def raiz(radicando,raiz=2):
    if radicando>0:
        r=radicando**(1/raiz)
        return r
    else:
        return("error:)")

def potencia(base,potencia):
    r=base
    for i in range(potencia-1):
        r*=base
    return r

def factorial(n):
    r=1
    for i in range(n):
        r+=r*i
    return r

def sumatoria(nI,nF):
    r=0
    for i in range(nI,nF+1):
        r+=i
    return r
