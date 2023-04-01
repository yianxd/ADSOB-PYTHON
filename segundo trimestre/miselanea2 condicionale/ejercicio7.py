horas=int(input("Ingrese las horas trabajadas: "))
if horas<=40:
    print("El salario es de: ",horas*2600)
else:
    h_extra=horas-40
    horas=horas-h_extra
    print("el salario es: ",(horas*2600)+(h_extra*5000))