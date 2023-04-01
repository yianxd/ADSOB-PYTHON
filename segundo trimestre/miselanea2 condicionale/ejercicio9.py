from datetime import date, time, datetime


print("-INGRESE UNA FECHA-")
dia=int(input())
mes=int(input())
año=int(input())
fecha=date(año,mes,dia)
f_actual=date.today()
if fecha<f_actual:
    diferencia=f_actual-fecha
    print("Desde la fecha introducida han pasado",diferencia.days)
else:
    diferencia=fecha-f_actual
    print("Faltan",diferencia.days,"para que llegue a esa fecha")

