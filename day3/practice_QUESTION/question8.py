n = 10
arr = [True for i in range(0,11)]
arr[0] = arr[1] = False
# print(arr)

for i in range(2,11):
    if(arr[i]==True):
        for j in range(i,11,i):
            if(j!=i):
                arr[j] = False
    print()
    
for i  in range(0,11):
    print(i,arr[i])