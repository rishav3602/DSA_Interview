## Find the index of a given element in an array using linear search

def linearSearch(arr,x):
    if len(arr) == 0:
        return "Array is empty"

    else:
        for i in range (len(arr)):
            if arr[i] == x:
                return i
    
    return -1

array = [1,2,3,4,5,6,7,8,9]
output = linearSearch(array,3)
print(f"The index of the given element is : {output}")