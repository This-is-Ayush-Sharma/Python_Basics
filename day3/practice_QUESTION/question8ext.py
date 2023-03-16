
arr = []

def FindPrime(n):
    global arr
    arr = [True if(i>1) else False for i in range(0,n+1)]
    for i in range(2,n+1):
        if(arr[i]==True):
            for j in range(i,n+1,i):
                if(j!=i):
                    arr[j] = False

n = int(input())+8
FindPrime(n)
sum = 0
for i in range(n-8,n+1):
    for j in range(i,0,-1):
        if(arr[j] == True and i%j == 0):
            sum+=j
            break
print(sum)