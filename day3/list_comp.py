# list comprehension

# for loop version
result = []
for i in range(11):
    result.append(i)
print(result)

# list comprehension
# resultant is a list
list_data = [int(i) for i in range(11)]
print(list_data)


# add all odd elements
odd_list = []
for i in range(11):
    if(i%2==1):
        odd_list.append(i)
print(odd_list)

#add all odd element
odd_element_list = [int(i) for i in range(11) if(i%2==1)]
print(odd_element_list)


# add all odd number else do the sq and append
combo_list = []
for i in range(11):
    if(i%2==1):
        combo_list.append(i)
    else:
        combo_list.append(i**2)
print(combo_list)

# same using list comprehension
combo_element_list = [int(i) if(i%2==1) else i**2 for i in range(11)]
print(combo_element_list)



print()  # make spaces
print()
mat = [
        [1,2,3,4],
        [5,6,7,8], 
        [9,10,11,12], 
        [13,14,15,16]
    ]
oneD = []
for i in range(0,len(mat)):
    for j in range(0,len(mat[0])):
        if(mat[i][j] % 2==0):
            mat[i][j] = (mat[i][j]**3)
        else:
            mat[i][j] = (mat[i][j]**2)

print("Result",mat)
mat = [
        [1,2,3,4],
        [5,6,7,8], 
        [9,10,11,12], 
        [13,14,15,16]
    ]
mat = [[j**3 if(j%2 == 0) else j**2 for j in i] for i in mat] 
print("after change", mat)