#q7
ls = []
for x in range(10):
    num = int(input("enter a number"))
    if num %2 == 0:
        ls.append(num)
print(sum(ls) / len(ls))
        
