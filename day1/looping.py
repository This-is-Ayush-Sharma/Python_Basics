# for loop

# range function
# range(start, end, step)

# number from 1 to 100
print("Number from range 1 to 100 all")
for i in range(1, 101):
    print(i,end=' ')

print()

# odd number from 1 to 100
print("Number from range 1 to 100 Odd Number")
for i in range(1,101,2):
    print(i,end=' ')

print()

# all even numbers from 1 to 100
print("Number from range 1 to 100 Even Number")
for i in range(2,101,2):
    print(i, end=' ')

print()



# reverse order
print("Number from range 100 to 1")
for i in range(100, 0, -1):
    print(i, end=' ')
print()