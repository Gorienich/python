#q1
def avgNum(a,b,c):
        if (a > b and a < c) or (a < b and a > c):
                return(a)
        if (b > a and b < c) or (b < a and b > c):
                return(b)
        else:
                return(c)
#q2
def sort3(a,b,c):
        ls =[a,b,c]
        print (min(ls))
        print(avgNum(ls[0], ls[1], ls[2]))
        print(max(ls))
        return max(ls)
#q3
def sort4(a,b,c,d):
    ls = [a,b,c,d]
    temp=0;
    for i in range(0,len(ls)-1):
            for j in range(i+1,len(ls)):               
                    if ls[i] < ls[j]:
                        temp = ls[i]
                        ls[i]=ls[j]
                        ls[j] = temp                   
    print(ls)
    print(max(ls))
#q4
def sortList( ls):
    temp=0;
    for i in range(0,len(ls)-1):
            for j in range(i+1,len(ls)):               
                    if ls[i] < ls[j]:
                        temp = ls[i]
                        ls[i]=ls[j]
                        ls[j] = temp
    print(ls)
    return tuple(ls)
#q5
def average(ls):
        return (sum(ls) / len(ls))
#q6
def AlmostAverage(ls):
        avg = abs(average(ls))
        val = abs(ls[0] - avg)
        for x in range( 1, len(ls)):
            if abs(ls[x] - avg) < val :
                    val = abs(ls[x] - avg)
                    ret = abs(ls[x])
        return ret
#q7
def defString(a,b,c="",d=""):
    print(d,c,b,a)
#8
def AllprimaryNum(num):
    ls = []   
    for x in range(3,num+1):
        for y in range(2,x):
            flag = True
            if x%y == 0:
                flag = False
                break
        if flag:
            ls.append(x)
    return tuple(ls)
#q9
import random
def Get_n(n):
        i = 0
        ls = []
        while i < n:
                ls.append(int(input("enter a number")))
                i +=1
        print(ls)
        for x in range(len(ls)):
                if ls[x] % 2 == 0:
                        ls[x] += random.randint(-10,20)
        print(ls)
#q10
def Divide(num):
        ls = []
        for x in range(1,num):
                if num % x == 0:
                        ls.append(x)
        print(ls)
        return(sum(ls))
#q11
def Meshuclal(num):
        if Divide(num) == num:
                return True
        else:
                return False
#q12
def Azeret(num):
        val = 1
        if num == 0 or num == 1:
                return 1
        else:
                for x in range(1,num+1):
                        val *= x
        return val
#q13
def Check_digit(num,digit):
        while num > 0:
                if num %10 == digit:
                        return True
                else:
                        num = int(num / 10)
        return False
#q14
def Count_sameDigits(num1,num2):
        ls = []
        while num1 > 0:
                if (Check_digit (num2, num1 %10)):
                            ls.append(num1 %10)
                num1 = int(num1/10)
        return ls
#q15  help in class
def secretString(s):
        val = ""
        for x in range(len(s)-1):
                if  s[x + 1] != s[x] and s[x] >= 'a' and s[x] <= 'z' or s[x] >= 'A' and s[x] <= 'Z':
                       val = val + s[x]
        return val
#q16
def min_list(ls):
        minVal = ls[0]
        index = 0
        for x in range(1,len(ls)):
                if ls[x] < minVal:
                        minVal = ls[x]
                        index = x
        print (index)
        return minVal
#q17
def merge_2ARR(ls1, ls2):
        ls3 = []
        i = 0
        while i < len(ls1) and i < len(ls2):
                ls3.append(ls1[i])
                ls3.append(ls2[i])
                i+=1

        if (i+1) > len(ls1):
                while i < len(ls2):
                        ls3.append(ls2[i])
                        i +=1
        if (i+1) > len(ls2):
                while i < len(ls1):
                        ls3.append(ls1[i])
                        i +=1
        return ls3
#q18
def mergeSort_2ARR(ls1,ls2):
        ls1Check = []
        ls2Check =[]
        for x in range(len(ls1)):
                if ls1[x] % 2 != 0:
                        ls1Check.append(ls1[x])
        for i in range(len(ls2)):
                if ls2[i] % 2 == 0:
                        ls2Check.append(ls2[i])
        print(ls1Check, ls2Check)
        ls3 = ls1Check + ls2Check
        ls3.sort()
        return ls3
#q19
def onlyStr(ls):
        temp = []
        for x in ls:
                if type(x) == str:
                        temp.append(x)
        return tuple(temp)
#q20

#classWork
ls =[10,2,4,5,15,1,-55]
ls2 = [11,3,3,2,2,4,9,-1,-33]
s1 = set(ls) | set(ls2)
s2 = list(s1)
s2.sort()
print(tuple(s2))

