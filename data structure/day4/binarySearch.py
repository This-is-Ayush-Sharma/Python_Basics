
def BinarySearch(array, x, low, high):
    while(high >= low):
        mid  = (high + low)//2
        if(array[mid] > x):
            high = mid - 1
        elif(array[mid] < x):
            low = mid + 1
        elif (array[mid] == x):
            return mid
    return -1

if __name__ == '__main__':
    array = [2,4,0,1,9]
    array.sort()
    print("SOrted list",array)
    x = 1

    result = BinarySearch(array, x, 0, len(array)-1)
    if(result == -1):
        print("Element not found!")
    else:
        print(f"Element found at {result+1}")