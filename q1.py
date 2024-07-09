#Q1
a = int(input("enter x"))
b = int(input("enter y"))
c = int(input("enter z"))
#check beetwen number
if (a > b and a < c) or (a < b and a > c):
    print("beetwen bumber" + str(a))
else:
    if (b > a and b < c) or (b < a and b > c):
        print("beetwen bumber" + str(b))
    else:
        print("beetwen bumber" + str(c))
