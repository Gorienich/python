#13
ls = []
num = int(input("enter number"))

for x in range(2,int(num/2+1)):
    if num%x ==0:
        ls.append(x)
print(num)
print(ls)
