n1=int(input("Ingrese un valor: "))
n2=int(input("Ingrese un valor: "))
n3=int(input("Ingrese un valor: "))

if n1==n2==n3:
    print("todos son iguales")
elif n1==n2:
    print("el primero y segundo son iguales")
elif n1==n3:
    print("el primer valor y tercero son iguales")
elif n2==n3:
    print("el segundo y tercero son iguales")
else:
    print("no son iguales")
