s = "Lee Quan Yew"

arr = []
for i in s:
    if(i==' '):
        arr.append('')
    elif(i.isupper()):
        arr.append(ord(i)-64)
    else:
        arr.append(ord(i)-96)
print(arr)

arr = ['' if(i==' ') else (ord(i)-96 if(i.islower()) else ord(i)-64) for i in s]
print(arr)