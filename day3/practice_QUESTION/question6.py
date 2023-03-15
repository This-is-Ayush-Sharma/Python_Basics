def Find_sq_digit(n):
    sum = 0
    while(n!=0):
        sum += (n%10)**2
        n//=10
    return sum

# arr = input().split(",")
def rotate(string, direction):
    print(string,direction)
    if(direction == 0):
        # rotate clockwise
        print(string[-1]+string[:-1])
    else:
        # rotate antoclockWise
        print(string[2:]+string[:2])
arr = "rhdt:246,ghftd: 1246".split(",")

for i in arr:
    if(Find_sq_digit(int(i[i.index(':')+1:])) % 2 == 1):
        rotate(i[0:i.index(':')],1)
    else:
        rotate(i[0:i.index(':')],0)