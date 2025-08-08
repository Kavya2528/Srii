import time
class person_class:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def m1(self):
        print("Name is:",self.name)
        print("Age is:",self.age)
class employee_class(person_class):
    def __init__(self, name, age,eid,esal,design,company):
        super().__init__(name, age)
        self.eid=eid
        self.esal=esal
        self.design=design
        self.company=company
    def m2(self):
            super().m1()
            print("eid is :",self.eid)
            print("esal is :",self.esal)
            print("design is :",self.design)
            print("company is :",self.company)
class student_class(person_class):
    def __init__(self, name, age,sid,subject,marks):
        super().__init__(name,age)
        self.sid=sid
        self.subject=subject
        self.marks=marks
    def m3(self):
            super().m1()
            print("sid is:",self.sid)
            print("subject is:",self.subject)
            print("marks are:",self.marks)
e1=employee_class("srii",25,1001,29000,"s/w developer","HCL")
e1.m2()
print()
s1=student_class("Kavya",20,3001,"python",98)
s1.m3()
print()
time.sleep(2)
print("end of an application")
print ("name of the user:",kavyasrii)
print("hello")



