#ejercicio 7 ciclos
def suma(num):
    a=0
    suma=0
    while suma<num:
        a+=1
        suma=suma+a
        print(suma)
#ejercicio 9
def potencia(base,exponente):
    resultado=1
    for i in range(exponente):
        resultado*=base
    return resultado


#ejercicio 13 ciclos
def num_inverso(num):
    num2=num
    r_num=0
    while num>0:
        num3=num%10
        r_num=r_num*10+num3
        num=num//10
    return r_num
#ejercicio 8 ciclos
def multiplos_cinco(num):
    for i in range(1,num+1):
        if i%5==0:
            print(i)
#ejercicio 3 ciclos

def n_perfecto(num):
    divisores=0
    for i in range(1,num):
        if num%i==0:
            divisores+=i 
    if divisores==num:
        return num
    else:
       return None
