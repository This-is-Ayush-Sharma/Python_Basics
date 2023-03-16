# a = input()
# b = input()

a = "I like Python"
b = "Java is a very popular language"

maxWords = a if(len(a)>len(b)) else b
minWords = a if(len(a)<len(b)) else b

arr = []

for i in minWords:
    if(i in maxWords and i not in arr and i!=' '):
        arr.append(i)

print(''.join(arr))