# categories of function

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