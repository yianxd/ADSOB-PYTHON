from datetime import *

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
        
    def getPassword(self):
        return self.__password
    
    def actualizarName(self,NewName):
        self.name = NewName
    
    def actualizarNum(self,NewNum):
            self.contactnum = Newnum
    
    def actualizarAge(self,NewAge):
            self.name = NewAge
            
    def actualizarPassword(self,NewPass):
            self.__name = NewPass


class Instructor(Usuarios):
    num_ins=0
    def __init__(self, id, name, age, brithDay, contactnum,password,credentials):
        Usuarios.__init__(self,id, name, age, brithDay, contactnum,password)
        self.__class__.num_ins+=1
        self.credentials=credentials
        self.courser=[]
        self.__username="instructorN"+str(self.__class__.num_ins) #buscar manera de usar la variable de clase para generar el usuario
        
    def verCredenciales(self):
        print(f"su username es: {self.__username}")

    def addCourse(self,curso):
        if curso not in self.courser:
            self.courser.append(curso)
        else:
            pass


class Students(Usuarios):
    num_st=0
    def __init__(self, id, name, age, brithDay, contactnum, password):
        self.__class__.num_st+=1
        Usuarios.__init__(self, id, name, age, brithDay, contactnum, password)
        self.courser=[]
        self.__username="EstudianteN"+str(self.__class__.num_st)

    def verCredenciales(self):
            print(f"su username es: {self.__username}")

    def getCourse(self,cursos):
        for i in cursos:
            print(i.description,i.yearlevel)

class Enrollment:
    def __init__(self,id,details,requirements):
        self.id=id
        self.details=details
        self.requirements=requirements
        self.date=datetime.today()

class Subjects:
    def __init__(self,id,name,description,schedule):
        self.id = id
        self.name = name
        self.description = description
        self.ins=[]
        self.schedule=schedule

    def addInstructor(self,inst):
        self.ins.append(inst)

        
class Course:
    def __init__(self,id,description,date,yearlevel):
        self.id=id
        self.numStudents=[]
        self.description=description
        self.date=date
        self.l_instructor=[]
        self.enrollments=[]
        self.c_subjets=[]
        self.yearlevel=yearlevel

    def generate_enrollment(self,id, details, requirements):
        if len(self.numStudents)<=6:
            enrol=Enrollment(self.id, details, requirements)
            self.enrollments.append(enrol)
        else:
            print("cantidad maxima de estudiantes")

    def addSubjets(self,subj):
        self.c_subjets.append(subj)

    def addInstructor(self,instructor,asignatura):
        for i in asignatura.values():
            if type(i) is list:
                for j in i:
                    if type(j) is dict:
                        for k in j.keys():
                            if k=="name":
                                for l in j.values():
                                    if instructor not in self.l_instructor:
                                        self.l_instructor.append(instructor)
                            else:
                                continue
                                    
                    else:
                        print("el instructor no puede dar esta asignatura")


ob1=Instructor(12, "a", 31, "as22", 13213, "asafdsd","algo con eso")
ob2=Instructor(13, "av", 32, "as2d2", 13214, "assfdsd","algo con eso")
ob3=Students(12, "b", "18", "1241", 13223, "safsfdfs")
curso1=Course(1, "python intermedio","12/12/12", "tercerTrimestre")
curso2=Course(2,"java god", "12/11/12", "CuartoTrimestre")
list_course=[curso1,curso2]
OOP=Subjects(212, "OOP", "En este curso se vera todo lo relacionado con programacion orientada a objetos", "cronograma")
OOP.addInstructor(ob1.__dict__)
curso1.addInstructor(ob1.name, OOP.__dict__)
curso1.addInstructor(ob1.name, OOP.__dict__)
curso1.addInstructor(ob2.name, OOP.__dict__)
ob1.addCourse(curso1)
print(OOP.__dict__)
print(curso1.__dict__)
print(ob1.__dict__)
#ob3.agregarCursos(curso1)
#ob3.verCredenciales()
#ob1.verCredenciales()
#ob2.verCredenciales()
#ob3.getCourse(list_course)
#curso1.addSubjets(OOP)