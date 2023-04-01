from Empresa import *
import csv

empresas=[]

with open('tercer trimestre/enterprises.csv') as a:
    b=csv.reader(a)

    for i in b:
        emp=empresa(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8])
        empresas.append(emp)

#----------------------------------------------------------

print("---Consultar datos---\n funciones: \n 1.buscar empresa por fecha de fundacion \n2.buscar empresas por index\n 3.buscar empresa por nombre ")
menu=input("que accion desea realizar?")

while true:
    match menu:
        case 1:
            a=input("buscar empresas por fundacion: ")
            for i in empresas:
                if i.getFounded()==a:
                    print(f"la empresa {i.getName()} se fundo en {i.getFounded()}")
        case 2:
            a=input("Buscar empresas por index: ")
            for i in empresas:
                    if i.getIndex()==a:
                        print(f"el numero de index corresponde a{i.verTodo()}")
        case 3:
            a=input("Buscar empresa por nombre: ")
            for i in empresas:
                if i.getName()==a:
                    print(f"la empresa que quiere ver es: {i.getName()} con los siguientes datos {i.verTodo()}")

