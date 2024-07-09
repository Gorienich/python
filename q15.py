#q15
count = 0
num = int(input("enter a number"))
for x in range(2,int(num/2+1)):
    if num%x ==0:
        count+=1
print(str(count),", numbers")

