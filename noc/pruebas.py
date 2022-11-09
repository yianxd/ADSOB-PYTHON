def c(num):
    if num>=1:
        print("es positivo")
    elif num<=-1:
        print("Es negativo")
    else:
        print("es 0")
def temperatura(celius):
    print("Temperatura en fahrenheit",(celius*9/5)+32)
    print("tempeturatura en kelvin=",celius+273.15)
    print("temperatura en rankine=",(celius*9/5)+491.67)

celius=float(input("Ingrese la temperatura en celius actua: "))
temperatura(celius)