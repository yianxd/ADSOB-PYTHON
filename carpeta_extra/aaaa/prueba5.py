class persona:
    def hablar(self):
        print("un dialogo")
        
class perro:
    def hablar(self):
        persona().hablar()

obj=persona()        
ob1=perro()
ob1.hablar()
