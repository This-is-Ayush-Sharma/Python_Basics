
def SelectionSort(arr):
    for i in range(0,len(arr)):
        for j in range(i+1, len(arr)):
            if(arr[i] > arr[j]):
                arr[i], arr[j] = arr[j], arr[i]
    return arr

if __name__ == "__main__":
    arr = [5,4,3,2,1]
    print("Original Array",arr)
    print("The sorted arr is",SelectionSort(arr))