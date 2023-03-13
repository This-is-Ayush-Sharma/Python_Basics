# Decision making statement

# read a number --> multiple of 3 
              # --> multiple of 5
              # --> multiple of both

# input function by default gets a string value 

number = int(input("Enter a number:-"))

if(number % 3 == 0 and number % 5 == 0):
    print("Both")

elif(number % 3 == 0):
    print("Multiple of 3")

elif(number % 5 == 0):
    print("Multiple of 5")

else:
    print("Invalid Input")