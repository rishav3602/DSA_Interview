### Binary search without recurssion

def binarySearch(arr,x):
    i = 0
    j= len(arr) - 1
    while i < j:
        mid = i + (j-i)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            i = mid+1
        else:
            j = mid - 1

    return -1

array = [1,2,3,4,5,6,7,8,9]
output = binarySearch(array,5)
print(f"The given element is here : {output}")
