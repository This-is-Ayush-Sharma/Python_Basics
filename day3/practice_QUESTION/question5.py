s = "3,2,6,5,1,4,8,9"

arr = list(map(int, s.split(",")))
print(arr)

data = sum(arr[0:arr.index(5)]+arr[arr.index(8)+1:])
print(data)
d = 0
for i in arr[arr.index(5):arr.index(8)+1]:
    d = d*10 + i
print(d)
print(data+d)