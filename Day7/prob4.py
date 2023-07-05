## sort any given array using bubble sort technique

def bubblSort(arr):
    n = len(arr) 
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]

    return arr

array = [546,23,58,3662,7474,24,49,25]
output = bubblSort(array)
print(f"Your sorted array using bubble sort is : {output}")
