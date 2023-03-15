mylist = [9,3,6,1,5,0,8,2,4,7]
list_b = [6,4,6,1,2,2]

dictr = {}
for i in list_b:
    dictr[i] = mylist.index(i)
print(dictr)

dictr = { i:mylist.index(i) for i in list_b }
print(dictr)
