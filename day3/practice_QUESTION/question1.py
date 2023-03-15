mylist = [9,3,6,1,5,0,8,2,4,7]
list_b = [6,4,6,1,2,2]

# without list comprehension
arr = []
for i in list_b:
    arr.append(tuple([i,mylist.index(i)]))
print(arr)

# with list comprehension
arr_data = [tuple([i,mylist.index(i)]) for i in list_b]
print(arr_data)