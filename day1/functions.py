# functions

# def <fn_name>()
# def <fn_name>(<parameters>, <parameters>)

# without parametres
def function1():
    print("Function 1")
function1()

# print() __str__  magical object to convert everything to string and pass the value as parameter

# with parameters
def function2(num1, num2):
    print("num1:-",num1,"num2:-",num2)
function2(10,30)


# with parameters with return type
def function3(num1, num2):
    return num1 + num2
print("Value returned:-", function3(10,30))


# with parameters with return type with int, float
def function4(num1, num2):
    return num1 + num2
print("Value returned:-", function4(10, 20.3))

# with parameters with return type with str, int
def function5(num1, num2):
    num1 = int(num1)
    return num1 + num2
print("Value returned:-", function5('10', 20))

# with parameters with return type with str, int
def function6(num1, num2):
    num2 = str(num2)
    return num1 + num2
print("Value returned:-", function6('10', 20))