string1 = 'Hello'
string2 = 'Elizabeth'

index1 = range(len(string1))
index2 = range(len(string2)) 
test = 0
test1 = 0

for i in index1:
    test = i
for i in index2:
    test1 = i
    
if test >= test1:
    for i in index1:
        try:
            print(string1[i], string2[i])
        except:
            print(string1[i])
else:
    for i in index2:
        try:
            print(string1[i], string2[i])
        except:
            print(' ',string2[i])