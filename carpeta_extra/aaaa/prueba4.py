class cls1:
    pass 

class cls2(cls1):
    pass 

ob1=cls2()
ob2=cls1()
ob3=cls2()
a=ob1
print(isinstance(ob1,cls1))
print(isinstance(ob2,cls2))
print(issubclass(cls2, cls1))
print(issubclass(cls1, cls2))

print(ob1 is a)