# שאלה1
#1 יצירת דיקשנרי שמפתחןת זה שמות אדנן ו בוב ומשמאות זה מדינות 
dic = {'admin':'jordan', 'bob':'England'}
# מדפיסים מפתחות ו משמאות של כל הדיקשנארי
print(dic)
#3 מדפיסים משמאות לפי מפתח
#dic['adnan']
#4 להוסיף מפת בן אם משמאות יו אס אי
dic['ben'] = 'usa'
#5 print again all keys and all values
print(dic)
#6 print value by keyName 'ben'
dic['ben']
#7 delate value by keyName 'adnan'
#del dic['adnan']
#8 print all keys and all values again
print(dic)
#9 new key 'bob' and value 'spain'
dic['bob'] = 'spain'
#10 print all keys and all values
print(dic)
#11 boolean return if dic has key 'ben'
'ben' in dic
#12 the same operation
'jordan' in dic
#13 print all keys
dic.keys()
#14 print all values
dic.values()
#15 delate all dictionary
dic.clear()
#16 create new dictionary dic2 BUT without last key and value BECAUSE it can't be same keys
dic2 = {'adnan':'jordan' , 'bob':'england' , 'adnan':'jordan'}
#17 print value by key 'adnan'
dic2['adnan']


#שאלה 2
dict = {'a1':(1,2), 'a2':(1,4), 'a3':(2,2), 'b1':(4,5),
        'b2':(2,4), 'b3':(2,5)}
#א function to print key and sum of value (x+y)
def sumX_Y (dict):
    for x in dict:
        print('point: ' , x, ' x+y = ', sum(dict[x]))
              
sumX_Y(dict)

#ב function to print point name and printing amount of stars by sum of value
def starX_Y (dict):
    for x in dict:
        print('point: ' , x , end='\t')
        for y in range(sum(dict[x])):
            print('*',  end='\t')
        print('\n')
              
#starX_Y(dict)

#ג function sort by X min-max
def sort_X(d):
  sorted_list = sorted(d.items(), key=lambda x: x[1][0])
  for k, v in sorted_list:
    print(k, v)
#sort_X(dict)

#ד function sort by Y if same Y sort by X
def sort_Y(d):
    sorted_dict = sorted(dict.items(), key=lambda x: (x[1][1], x[1][0]))
    print(sorted_dict)
#sort_Y(dict)

# ה function to add new point by sum y+y1 and x+x1
l1= (1,2)
l2= (3,6)
def newPoint(d, l1,l2):
    d['A' + str(len(d))] = (int((l1[0] + l2[0])/2) , int((l1[1] + l2[1])/2))
    print(d)
    
#newPoint(dict, l1,l2)

#שאלה 3 set
a = set([21,4,8,10,14,23,4]);
b = set([20,12,43,23,5,4])
# א print A ,B
print(a)
print(b)
# ב function to print union numbers
def unionSET(a,b):
    ls=[]
    for x in a:
        for y in b:
            if x==y:
                ls.append(x)
    print(set(ls))
#unionSET(a,b)
    
# ג function to print intersection of a,b
def intersecSET(a,b):
    ls=[]
    for x in a:
            if x not in b:
                ls.append(x)
    print(set(ls))
#intersecSET(a,b)

#ד function to print abs between a,b each number
def absSET(a,b):
    print(a.intersection(b))
#absSET(a,b)

# ה marge of a,b
def margeAB(a,b):
    c = a.union(b)
    print(sorted(c))
#margeAB(a,b)

# ו same foo as abs

# ז foo to add something in set and print setlist
c = 111
def someADD(a, c):
    a.add(c)
    print(a) 
#someADD(a, c)

# ח foo to add a few numbers
ls = [22,33,34,35]
def moreADD(a,ls):
    for x in ls:
        a.add(x)
    print(a)
#moreADD(a,ls)

#י foo to pop() setlists and make new one with 2 numbers
def newSET(a,b):
    
    num1 = a.pop()
    num2 = b.pop()
    ls = [num1, num2]
    print(ls)
#newSET(a,b)

#יא add b to c
c= set([0,0,0])
def addNumbers(a,c):
    for x in c:
        a.add(x)
    print(a)
#addNumbers(a,c)

# שאלה 4
lt1 = [23,'m','d',235,'t','x',15]
lt2 = ['the', 'method', 34, 't', 'go',23]
# fun return 2 tupples sorted numbers without repeat and intersection of strings
def twoTUPPLES(lt1,lt2):
    #choose numbers
    lsNum = []
    lsSTR = []
    a = [i for i in lt1 if isinstance(i, int)]
    b = [i for i in lt2 if isinstance(i, int)]
    for x in a:
        if x not in b:
            lsNum.append(x)
    for x in b:
        if x not in a:
            lsNum.append(x)
    #choose str
    a = set([i for i in lt1 if isinstance(i, str)])
    b = set([i for i in lt2 if isinstance(i, str)])
    lsSTR = set(a.intersection(b))
    #create set
    c = [lsSTR,set(lsNum)]
    return c


print(twoTUPPLES(lt1,lt2))
