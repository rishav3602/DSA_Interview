## Apply binary search in a given 2d array

def binarySearch2d(arr,x):
    m = len(arr) 
    if m == 0:
        return "The given array is empty cannot apply this algo"
    
    n = len(arr[0])

    start  = 0
    end = m*n - 1
    while start <= end:
        mid_index = start + (end- start)//2
        mid_element = arr[mid_index//n][mid_index%n]

        if mid_element == x:
            return mid_index
        elif mid_element < x:
            start = mid_element +1
        else:
            end = mid_element -1

    return -1

array = [[1,2,3],[4,5,6],[7,8,9]]
output = binarySearch2d(array,5)
print(f"The given element is at this index : {output}")
