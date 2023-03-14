def find_count(number, CountOff):
    count = 0
    while(number != 0):
        if(number % 10 == CountOff):
            count+=1
        number=number//10
    return count
def CheckDouble(number):
    number_double = 2*number
    for i in range(0,10):
        if(find_count(number, i) != find_count(number_double,i)):
            return False
    return True

print(CheckDouble(125874))
print(CheckDouble(123))