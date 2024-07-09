class Person:
    tz = 0
    name = "no name"
    cnt = 1
    
    def __init__(self, name = "No name", tz=10000):
        self.name = name 
        self.tz = tz + Person.cnt
        Person.cnt += 1

    def Print(self):
        print( self.name, "id:", self.tz)

class Citizen:
    pass

class Student(Person, Citizen) :  # ירושה מרובה אפשרית בפייתון
    sakhar = 12000
    cls  = "No classroom"
    age = 0

    def __init__(self, age, name , cls = "Noo Classroom"):
        self.age = age
        self.cls = cls
        super().__init__(name)
        self.name = self.name + self.name       

    def setSakhar(self, skhr):
        self.sakhar = skhr

    def assignCls(self, cls):
        # הוצאת התלמיד מהכיתה הנוכחית
        # הכנסת התלמיד לכיתה החדשה
        self.cls = cls

    def __str__(self):
        return str(self.cls) + self.name + str(self.age)
    
