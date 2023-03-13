# control statement


# break 


# wap 1 to 100 print data less than 50 then break
print("Example of break statement")
for i in range(1, 101):
    if(i > 49):
        break
    print(i, end = ' ')

print()


# continue
print("Example of continue statement")
for i in range(1, 101):
    if(i == 50):
        continue
    print(i, end = ' ')

print()