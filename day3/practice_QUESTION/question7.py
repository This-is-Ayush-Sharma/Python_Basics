import math

def isPrime(n):
    if(n<2):
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if(n%i == 0):
            return False
        
    return True

def find_Factor(n):
    for i in range(n,0,-1):
        if(isPrime(i) and n%i == 0):
            return i
        
n = int(input())
sum = 0
for i in range(n,n+9):
    sum+=find_Factor(i)

print(sum)