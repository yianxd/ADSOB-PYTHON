class Usuarios:
    def __init__(self,id,name,age,contactnum,username,password):
        self.id = id
        self.name = name
        self.age = age
        self.contactnum = contactnum
        self.__username = username
        self.__password = password
        
    def getPassword(self):
        return self.__password

    def getUsername(self):
        return self.__username

    def actualizarName(self,NewName):
        self.name = NewName
    
    def actualizarNum(self,NewNum):
            self.contactnum = Newnum
    
    def actualizarAge(self,NewAge):
            self.name = NewAge
            
    def actualizarPassword(self,NewPass):
            self.__name = NewPass


class Instructor(Usuarios):
    def __init__(self,id, name, age, contactnum, username, password,credentials):
        Usuarios.__init__(self, id, name, age, contactnum, username, password)        
        self.credentials=credentials

class Students(Usuarios):
    def __init__(self,id, name, age, contactnum, username, password):
        Usuarios.__init__(self, id, name, age, contactnum, username, password)
        self.course=[]

    def viewCourse(self,curso):
        for i in curso:
            print(i.description)
    
    def admit(self,course):
        if course.enrollment!="":
            self.course.append(course)



class Subjects:
    def __init__(self,id,name,description):
        self.id = id
        self.name = name
        self.description = description
        self.instructor=""
        self.schedule=""

    def addInstructor(self,instructor):
        self.instructor=instructor
    
    def scheduling(self,schedule):
        self.schedule=schedule

class Enrollment:
    def __init__(self,id,details,requirements,date):
        self.id=id
        self.details=details
        self.requirements=requirements
        self.date=date
        
class Course:
    def __init__(self,id,description,date,yearlevel):
        self.id=id
        self.description=description
        self.date=date
        self.yearlevel=yearlevel
        self.subject=[]
        self.enrollment=""
    def setId(self,NewId):
        self.id=NewId

    def setDescription(self,NewDesc):
        self.description=NewDesc
    
    def setDate(self,NewDate):
        self.date=NewDate
    
    def setYearLevel(self,NewY):
        self.yearlevel=NewY

    def addSubjets(self,curso):
        self.subject.append(curso)

    def generateEnrollment(self):
        enr=Enrollment(1, "6 estudiantes para curso java", self.yearlevel, "hoy hasta 9/03/2023")
        self.enrollment=enr

    def getEnrollment(self):
        return enrolment


ob1=Instructor(123, "A", 32, 3212, "a123", "fdfdss", "diplomado expedido en ...")
curso1=Course(1, "descripcion del curso", "08/03/23-23/04/23", "conocimientos basicos en python")
subj1=Subjects(1, "python", "python intermedio")
ob2=Students(124, "b", 18, 4313, "b123", "dfghjk")
cursos=[curso1]
#----------
curso1.addSubjets(subj1)
subj1.scheduling("el cronograma es...")
subj1.addInstructor(ob1)
curso1.generateEnrollment()
ob2.viewCourse(cursos)
ob2.admit(curso1)
print(ob2.__dict__)