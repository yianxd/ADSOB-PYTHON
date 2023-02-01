n1=int(input("Ingrese un valor: "))
n2=int(input("Ingrese un valor: "))
n3=int(input("Ingrese un valor: "))

if n1>n2:
    if n1<n3:
        print("n1 es el numero del medio",n1)
    elif n3>n2:
        print("n3 es el numero del medio",n3)
    elif n1>n2:
        print("n2 es el numero del medio", n2)
elif n2<n3:
    print("n2 es el numero del medio", n2)
elif n3<n2:
    if n1<n2:
        print("n1 es el numero del medio", n1)
    elif n2>n3:
        print("n3 es el numero del medio",n3)
    else:
        print("n1 es el numero del medio", n1)
