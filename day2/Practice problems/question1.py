

# output returns a list [no of characters, no of digits]

def CountMethod(s):
    list = [0,0]

    for i in s:
        if(i.isdigit()):
            list[1]+=1
        if(i.isalpha()):
            list[0]+=1
    

    return list


data = input("Sample input:- ")
print(CountMethod(data))
