## Binary search in a 2D array

def binarySearchMatrix(arr,x):
    m = len(arr)
    if m == 0:
        return False
    
    n = len(arr[0])

    start = 0
    end = m*n -1

    while start < end:
        mid = start +(end-start)//2
        mid_element = arr[mid//n][mid%n]
        if mid_element == x:
            return True
        elif mid_element < x:
            start = mid+1
        else:
            end = mid - 1

    return False

array = [[1,2,3],[4,5,6],[7,8,9]]
x = 5
output = binarySearchMatrix(array , x)
print(output)