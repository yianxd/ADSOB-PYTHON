class Usuarios:
    num_u=0
    def __init__(self,id,name,age,brithDay,contactnum,password):
        self.__class__.num_u+=1
        self.id = id
        self.name = name
        self.age = age
        self.brithDay = brithDay
        self.contactnum = contactnum
        self.__password = password

class dos:
    def __init__(self):
        self.valor=[]
    def agregar(self,nuevo):
        self.valor.append(nuevo)

        

#ob1=Usuarios(1, "a", 12, "asad", 1234, "fghjkl")
#ob2=dos()
#ob2.agregar(ob1.__dict__.values())

#print(ob2.valor)

a={ "a":2,"b":3,"c":[{"id":12,"name":"a"}]

}
b="a"
c=[]
for i in a.values():
    print(i)
    if type(i) is list:
        for j in i:
            print(i,j)
            if type(j) is dict:
                for k in j.keys():
                    if k=="name":
                        for l in j.values():
                            print(l)
                            if l not in c:
                                c.append(b)

print(c)