list = []


# to find the sum of a pair of nummber t0 obtain sum equal to number

def Pair(list, number):
    for i in range(0,len(list)-1):
        for j in range(i+1, len(list)):
            if((list[i] + list[j]) == number):
                print("(",list[i],",",list[j],")",sep='',end=' ')
    print()

Pair([1,2,7,4,5,6,0,3],6)
Pair([3,4,1,8,5,9,0,6],9)