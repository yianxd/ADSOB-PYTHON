angulo=int(input("Ingrese un angulo: "))
vuelta=1
pi=3.1415
if angulo<=360:
    print("a dado",vuelta,"vuelta")
    print("la medida en radianes es:",angulo*pi/180)
else:
    vuelta=vuelta+(angulo//360)
    print("a dado",vuelta,"vuelta")
    print("la medida en radianes es:",angulo*pi/180)