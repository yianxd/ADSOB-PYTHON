print("--CONTESTA BIEN LAS SIGUIENTES PREGUNTAS:D")
ryp=input("Colon descubrió América?")
if ryp=="si": 
    ryp=input("La independencia de Colombia fue en el año 1810?")
    if ryp=="no":
        ryp=input("The Doors fue un grupo de rock Americano?")
        if ryp=="si":
            print("ganaste")
            exit()
else:
    exit()
print("perdiste")