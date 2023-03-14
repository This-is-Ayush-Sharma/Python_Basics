n1 = int(input())
n2 = int(input())

array = [int(i) for i in range(n1,n2+1)]
print(array)

sub_array = [array[i:j+1] for i in range(0,len(array)) for j in range(i,len(array))]
# print(sub_array) 
count = 0
for i in sub_array:
    print(i,end=' ')
    if(sum(i)%2==1):
        count+=1
else:
    print()

print(count)
