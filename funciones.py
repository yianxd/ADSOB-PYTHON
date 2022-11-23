import datetime
def agregar_a(lst,art,canciones=""):
    lst["playlist"][art]={}
    lst["playlist"][art]["canciones"]={}
    return lst

def agregar_c(lista,artista,cancion,genero,duracion):
    if artista in lista["playlist"]:
        lista["playlist"][artista]["canciones"][cancion]={genero:duracion}
        return lista
    else:
        agregar_a(lista, artista)
        lista["playlist"][artista]["canciones"][cancion]={genero:duracion}
        return lista

def buscar_a(lista,artista):
    if artista in lista["playlist"]:
        return lista["playlist"]
    else:
        print("el artista no se encuentra en la lista")

def delete_a(lista,artista):
    if artista in lista["playlist"]:
        del lista["playlist"][artista]
        return lista
    else:
        print("el artista no se encuentra")

#def buscar_c(lista,cancion):
    for i in lista["playlist"]:
        for j in lista["playlist"][i]:
            if cancion in lista["playlist"][i]:
                return i
