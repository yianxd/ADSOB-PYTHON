from Empresa import *
import csv

empresas=[]

with open('C:\\Users\\AdminSena\\Pictures\\yian\\ADSOB-PYTHON\\actividad13-3-2023\\enterprises.csv') as a:
    b=csv.reader(a)

    for i in b:
        emp=empresa(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8])
        empresas.append(emp)

#----------------------------------------------------------
for i in empresas:
    lista=[]
    a="0"
    print(i.getFounded())
    if i.getFounded()>a:
        a=i
        lista.insert(0,a)
print(lista)
