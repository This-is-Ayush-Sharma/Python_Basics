

# output returns a list [no of characters, no of digits]

# used string.isdigit() and string.isalpha()
def CountMethod(s):
    list = [0,0]

    for i in s:
        if(i.isdigit()):
            list[1]+=1
        if(i.isalpha()):
            list[0]+=1
    return list

# without using built-in method
def CountMethod2(s):
    list = [0,0]
    for i in s:
        if((ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122)):
            list[0]+=1
        if(ord(i)>=48 and ord(i)<=57):
            list[1]+=1
    return list

data = input("Sample input:- ")

print(CountMethod(data))
print(CountMethod2(data))