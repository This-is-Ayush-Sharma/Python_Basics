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
sum=0
for i in range(11):
    if(i%2==1):
        odd_list.append(i)
print(odd_list)

#add all odd element
odd_element_list = [int(i) for i in range(11) if(i%2==1)]
print(odd_element_list)

