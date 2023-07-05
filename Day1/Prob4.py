## Returning the index of any given element from an array using linear search

def ret_index(arr , x):
    for i in range (len(arr)):
        if arr[i] == x:
            return i
        
    return -1
        
array = [1,2,3,3,44,46,3,432,24]
output = ret_index(array,24)
print(f"Your element is found at this index : {output}")