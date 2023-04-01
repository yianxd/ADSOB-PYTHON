numero = int(input("introduzca el numero: "))
i=1
divisores=0
for i in range(1,numero):
    if (numero % i) == 0 :
        divisores=divisores+i
if divisores==numero:
    print("es numero perfecto")
else:
    print("no es numero perfecto")