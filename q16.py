#q16
num = int(input("enter a number"))
flag = True
x=2
while x<(num/2) and flag:
    if num % x == 0:
        print(str(num), " is not a primary number")
        flag = False
    x+=1
if flag:
     print(str(num),", is a primary numbers")

