## Binary search with recurssion

def binarySearch(arr,i,j,x):
    while i <= j:
        mid = i + (j-i)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binarySearch(arr,mid+1,j,x)
        else:
            return binarySearch(arr,i,mid-1,x)
        
    return -1

array = [1,2,3,4,5,6,7,8]
i = 0
j = len(array) -1
output = binarySearch(array,i,j,5)
print(f"Your given element is at this position in the given array : {output}")
