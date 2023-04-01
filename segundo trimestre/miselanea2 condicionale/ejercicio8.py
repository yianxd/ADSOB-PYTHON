minutos=int(input("Cuando duro la llamada? "))
if minutos<=3:
    print("el coste es de: ", minutos*200)
else:
    print("el coste es de: ",(50*(minutos-3))+600)