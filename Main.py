from funciones import agregar_a, agregar_c, buscar_a, delete_a, orga
import datetime

lista={"playlist":{}}
print("---BIENVENIDO---\n","Que desea hacer?")
init="si"
while init=="si":
    entrada=input("Agregar artista\nagregar canciones\nbuscar artista\nbuscar cancion\neliminar artista\norganizar\n: ")
    entrada.lower()
    match init:
     case "agregar artista": 
        agregar_a(lista, input("Nombre del artista: "))
        entrada2=input("Quiere agregar otra?\nsi/no: ")
        entrada2.lower()
        while entrada2=="si":
            agregar_a(lista, input("Nombre del artista: "), " ")
            entrada2=input("Quiere agregar otra?\nsi/no: ")
            entrada2.lower()
        else:
            init=input("Desea continuar?\nsi/no: ")
            init.lower()
     case  "agregar canciones":
        agregar_c(lista, input("Ingrese el nombre del artista: "), input("Nombre de la cancion: "), input("Genero de la cancion:"), input("Duracion de la cancion: "))
        entrada2=input("Quiere agregar otra?\nsi/no: ")
        entrada2.lower()
        while entrada2=="si":
            agregar_c(lista, input("Ingrese el nombre del artista: "), input("Nombre de la cancion: "), input("Genero de la cancion:"), input("Duracion de la cancion: "))
            entrada2=input("Quiere agregar otra?\nsi/no: ")
            entrada2.lower()
        else:
            init=input("Desea continuar?\nsi/no: ")
            init.lower()
     case "buscar artista":
        entrada3=input("Ingrese el nombre del artista: ")
        print(buscar_a(lista, entrada3))
        init=input("Desea continuar?\nsi/no: ")
        init.lower()
     case "buscar cancion":
        entrada4=input("Ingrese el nombre de la cancion: ")
        #print(buscar_c(lista, entrada4))
     case "eliminar artista":
        entrada5=input("Ingrese el nombre del artista: ")
        print(delete_a(lista, entrada5))
        init=input("Desea continuar?\nsi/no: ")
        init.lower()
     case "organizar":
        print(orga(lista))
        

print(lista)