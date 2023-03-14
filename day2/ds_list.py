# list predefined data structure
# 1. ordered data structure (indexing is starts from 0)
# 2. mutable 


# empty list 
list1 = []
print(list1, type(list1))

#list with a integer values
list2 = [10,20,30,40]
print(list1, type(list2))

#list with multiple types
list3 = [10,3+7j,95.3,"ayush"]
print(list3,type(list3))

# list function
list4 = list([1,2,3,4,5])
print(list4,type(list4))


# append method to add data to list at the end
list5 = [1,2,3,5,5,7]
list5.append(88)
print("Example of append method",list5)

# extend method to add more than one data in the list extend([list])
list6 = [1,2,3,4,56,7]
list6.extend([22,59])
print("Example to extend",list6)

# insert method to insert a element to a particular index   insert(<position>,<value>)
list7 = [1,2,3,4,5,6]
list7.insert(2,55)
print("Insert operation",list7)

# example remove()
list8 = [1,2,3,4,5,67,8]
list8.remove(2)
print("After removing 2 from index 1", list8)
# if the element is present then only we can use remove function or else we get error

# pop method example
list9 = [1,2,3,4,5,6]
list9.pop()
print("After using only pop() method", list9)  # last value get deleted from the list
list9.pop(1)
print("After using pop(1) with index 1", list9)

# del method example
list10 = [1,2,3,4,5,6]
del list10[1]
print("del method example",list10)
