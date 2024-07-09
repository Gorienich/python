#q8-q9
lt = []
num = int(input("enter a number"))
maxNum = num
minNum = num
for x in range(9):
    num = int(input("enter a number"))
    if num > maxNum:
        maxNum = num
    if num < minNum:
        minNum = num
print(maxNum)
print(minNum)
