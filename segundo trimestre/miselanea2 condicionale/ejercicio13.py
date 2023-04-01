segundos=int(input("Ingrese una cantidad de segundos: "))
minutos=0

if segundos<=60:
    print("hay",minutos,"minutos y",segundos,"segundos")
else:
    minutos=segundos//60
    print("hay",minutos,"minutos y ",segundos%60,"segundos")
