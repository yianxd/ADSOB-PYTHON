print("-Ingrese la hora-")
hora=int(input())
minutos=int(input())
segundos=int(input())
if hora<=24 and minutos<=60 and segundos<=60:
    segundos+=1
print("tendro de un segundo seran las",hora,minutos,segundos,sep=":")