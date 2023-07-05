## Sort the given array using bubble sort

def bubbleSort(arr):
    n = len(arr) 
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1] :
                
                #swapping the elements
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
    
    return arr

array = [21,34,10,64,78,5,16]
output = bubbleSort(array)
print(f"Your sorted array using bubble sort is : {output}")