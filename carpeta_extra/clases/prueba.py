class Persona:
    def __init__(self, name,lastname,edad,id):
        self.name = name
        self.lastname = lastname
        self.edad = edad
        self.id = id
        
persona_1=Persona("Juan","Games",18,"12243434")

print(persona_1.__dict__)