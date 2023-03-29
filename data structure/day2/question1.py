
list1 = [11,8,23,7,25,15]
list2 = [6,33,50,31,46,78,16,25]

support = []

for i in list1:
    if(2*i in list2):
        support.append(i)

print(support)