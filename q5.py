#q5
x = int(input("enter number"))
y = int(input("enter number"))
result = int(max(x,y)/min(x,y))
div = max(x,y)%min(x,y)
print(str(max(x,y)), "/", str(min(x,y)), " = ",
          str(result), str(div), "/" ,
          str(min(x,y))) 
