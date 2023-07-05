## sort the given array with the help of insertion sort

def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1

        while j>= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j -1

        arr[j+1] = key

    return arr

    

array = [546,23,58,3662,7474,24,49,25]
output = insertionSort(array)
print(f"Your sorted array using insertion sort is : {output}")