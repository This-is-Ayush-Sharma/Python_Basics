n1 = int(input())
n2 = int(input())

arr = []
for i in range(n1, n2+1):
    arr.append(i)

print(arr)
count = 0
ar = []
for i in range(0,len(arr)):
    for j in range(i,len(arr)):
        ar.append(arr[j])
        print(ar,end=' ')
        if(sum(ar)%2==1):
            count+=1
    ar = []


print()
print(count)

