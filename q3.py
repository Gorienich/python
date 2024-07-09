#q3
# Get the input strings
ls = []

for i in range(4):
    ls.append(input("Enter a string:"))

count =0
st = ""
# Iterate through the list of strings and update the count for each string
for x in ls:
    if x in ls:
        
        count +=1
    else:
        st += x

print(st)
