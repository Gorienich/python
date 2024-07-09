# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Meroba:
    name = "MEROBA"
    cnt = 1
    __sog = 40

    def __init__(self, a, b, c, d, a1, a2, a3, a4=None):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        if a4 is None:
            self.a4 = 360 - self.a1 - self.a2 - self.a3
        else:
            self.a4 = a4
        self.name += '_' + str(Meroba.cnt)
        Meroba.cnt += 1

    def Hekef(self):
        return self.a+self.b+self.c+self.d

    def Ok_Z(self):  # זויות חוקיות
        s=self.a1 + self.a2 + self.a3+ self.a4
        if (s != 360):
            print("Zawaya problem in" , self.name, s, "!= 360 (sum)")
            return False
        return True

    def Ok_A(self):  # צלעות חוקיות
        if (  self.a > self.b + self.c + self.d or
                self.b > self.a + self.c + self.d or
                self.c > self.b + self.a + self.d or
                self.d > self.b + self.c + self.a ):
            print("Zlaot problem in", self.name, max(self.a, self.b, self.c, self.d), "bigger than sum of 3 others" )
            return False
        return True

    def Ok(self):
        if self.Ok_Z() and self.Ok_A() :
            return True
        return False

    def Print(self):
        print(self.name + ':(', self.__sog, ')', self.a, self.b, self.c, self.d, self.a1, self.a2, self.a3, self.a4)

#-----------------------------------------------------------------------

class Makbilit(Meroba):
    name = "MAKBILIT"
    __sog = 41
    def __init__(self, a, b, a1, a2):
#        super(Motawazi, self).__init__(a, b, a, b, a1, a2, a1, a2)
        super().__init__(a, b, a, b, a1, a2, a1, a2)


    def Ok_Z(self):  # זויות חוקיות
        s=self.a1 + self.a2 
        if (s != 180 or not super().Ok_Z()):
            print("Zawaya problem in" , self.name, s, "!= 180 (sum)")
            return False
        return True

    def Ok_A(self):  # צלעות חוקיות
        if ( self.a != self.c or self.b != self.d):
            print("Zlaot problem in", self.name,  " 2 not equal" )
            return False
        return True

#-------------------------------
class Malben(Makbilit):
    name = "MOSTATEL"
    __sog = 411
    def __init__(self, a, b):
        super().__init__(a, b, 90,  90)
#        super(Meroba, self).__init__( a, b,a, b, 90, 90, 90, 90)

    def Ok_Z(self):  # זויות חוקיות
        if (self.a == self.b == self.c == self.d == 90):
            return True;
        else:
            print("Zawaya problem in" , self.name)# min(a1, a2, a3, a4), "!= ", max(a1, a2, a3, a4))
            return False

# אין צורך בבדיקת צלעות כי אותה פקודה של מחלקת האבא
#   def Ok_A(self):  # צלעות חוקיות
#        if ( a != c or b != d):
#            print("Zlaot problem in", self.name,  " 2 not equal" )
#            return False
#        return True

#---------------------------------------
class Meoyan(Makbilit):
    name = "MEOYAN"
    __sog = 412
    
    def Ok_A(self):
        return self.a == self.b == self.c == self.d

#--------------------------
class Reboa(Malben, Meoyan):
        name = "MeRoBA3"
        __sog = 4111
        def __init__(self, a):
            super().__init__( a, a)
#            super(Moraba3 , self).__init__( a, a)

#--------------------------------
class Dalton (Meroba):
    name = "DALTON"
    __sog = 42
    def __init__(self, a, b, a1, a2, a3, a4=None):
        if a4 is None :
            d = 360 - a1 - a2 - a3
            if   d == a1:
                a4 = a3
                a3 = d
            elif d == a2:
                a4 = d
            elif d == a3:
                a4 = a1
                a1 = d
        super().__init__(a, b, b, a, a1, a2, a3, a4)

    def Ok_Z(self):
        if not super().Ok_Z():
            return False
        if not (self.a1 == self.a3 or self.a2 == self.a4 ):
            print(self.name, "problem no eqwal oppsit Zawya")
            return  False
        return True

    def Ok_A(self):
        if ( self.a != self.d and self.b != self.c):
            print("Zlaot problem in", self.name,  " 2 not equal" )
            return False
        return True

# ------------------------------------------


def execute():
    # Use a breakpoint in the code line below to debug your script.

    rb = Meroba(2, 4, 3, 5, 39, 141, 60, 120)
    if rb.Ok() :
        rb.Print()
    mt = Makbilit (2, 24, 39, 131)
    if mt.Ok() :
        mt.Print()
        mt.Hekef()
    ma = Malben( 16, 20)
    if ma.Ok() :
        ma.Print()
    dl = Dalton( 5, 9, 120, 40, 80)
    if dl.Ok() :
        dl.Print()
    dl2 = Dalton(6, 10, 120, 40, 90)
    if dl2.Ok():
        dl2.Print()
    mr = Reboa(17)
    print(mr.name, mr.Hekef())
    if mr.Ok() :
        mr.Print()
    mr2 = Reboa(11)
    mr2.cnt = 70
#    Roba3i.cnt = 50
    mr2.__sog = 3
    print(mr2.name, mr2.Hekef())
    if mr2.Ok():
            mr2.Print()
    m3 = Meoyan(32, 32, 110, 73)
    if m3.Ok() :
        print(m3.Hekef())
    rb3 = Reboa(12, 10, 23, 22, 90, 90, 100, 80)
    if rb3.Ok() :
        pass
    rb3.Print()




