## sort the given array using selection sort.

def selection_sort(arr):
    n = len(arr)    
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i] , arr[min_index] = arr[min_index] , arr[i]


    return arr


array = [45,23,78,10,16,34,23]
output = selection_sort(array)
print(output)