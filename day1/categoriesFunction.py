# categories of function


# values to the fuction is passed from right to left

# based on arguments

# Positional arguments
def function(num1, num2, num3, num4):
    print("num1:-", num1,"num2:-", num2,"num3:-", num3,"num4:-", num4)
function(1,2,3,4)
# function(100,200,300) # error less parameter typeError
# function(1,2,3,4,5) # error extra parameter typeError

# Keyword arguments
def function2(num1, num2, num3, num4):
    print("num1:-", num1,"num2:-", num2,"num3:-", num3,"num4:-", num4)

function2(num4 = 10, num1 = 20, num2 = 30, num3 = 40)

#default arguments

# default arguments should be followed by non default arguments
def function3(name , rollno, branch, collegename = "GIET"):
    print(name , rollno, branch, collegename)

function3("ayush", 11, "CSE")
function3("Venu", 13, "CST")

# function4 function can accept any number of arguments
def function4(*var):
    for i in var:
        print(i,end=' ')
    else:
        print()
function4(2,3,5,6)
function4(2,3,5,6,7,8,9)    

def add(*var):
    sum = 0
    for i in var:
        sum+=i
    else:
        print("Sum:-",sum)
add(2,3,5,6)
add(2,3,5,6,7,8,9)  