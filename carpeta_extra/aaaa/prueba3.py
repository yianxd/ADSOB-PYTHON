class Ser_vivo:
    def __init__(self,nombre,tiempo_v):
        self.nombre = nombre
        self.tiempo_v = tiempo_v
    
    def vivo(self):
        print("Todos estan vivos")
    def comer(self):
        print("todos los seres vivos comen:)")
#---------------------------
class Reino_animal(Ser_vivo):
    def __init__(self,nombre,tiempo_v):
        Ser_vivo.__init__(self,nombre,tiempo_v)
class Carnivoros(Reino_animal):
    pass 
class Felinos(Carnivoros):
    pass 
class Herbivoro(Reino_animal):
    pass
class Leporidae(Herbivoro):
    pass
#-------------------------- 
class Reino_vegetal(Ser_vivo):
    def __init__(self,nombre,tiempo_v):
        Ser_vivo.__init__(self,nombre,tiempo_v)
    
    def vivo(self):
        return super().vivo()

class Reino_Funji(Ser_vivo):
    def __init__(self,nombre,tiempo_v):
        Ser_vivo.__init__(self,nombre,tiempo_v)


class Reino_monera(Ser_vivo):
    def __init__(self,nombre,tiempo_v):
        Ser_vivo.__init__(self,nombre,tiempo_v)

class Reino_protista(Ser_vivo):
    def __init__(self,nombre,tiempo_v):
        Ser_vivo.__init__(self,nombre,tiempo_v)