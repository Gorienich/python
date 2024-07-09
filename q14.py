#q14
ls = []
low = int(input("enter low lvl"))
high = int(input("enter high lvl"))
for x in range(low,high):
    if x%3 ==0 and ("1" in str(x)):
        ls.append(x)
print(low,high)
print(ls)
