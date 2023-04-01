from datetime import time
print("-Ingrese la hora-")
hora=int(input())
minutos=int(input())
segundos=int(input())
if hora<=24 and minutos<=60 and segundos<=60:
    segundos+=1
    if segundos==60:
        segundos=0
        minutos+=1
        if minutos==60:
            minutos=0
            hora+=1
            if hora==24:
                hora=0
print(hora,minutos,segundos,sep=":")