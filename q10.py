a = int(input("enter low level"))
b = int(input("enter high level"))
ls = []
for x in range(10):
    num = int(input("enter a number"))
    if (num <= b) and (num >= a):
        ls.append(num)
print(a,b)
print(ls)
