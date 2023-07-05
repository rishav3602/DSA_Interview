## Find the index of a given element in an array


def binarySearch(arr, x):
    arr = sorted(arr)
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = start + (end-start)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1


array = [1,2,3,4,5,6,7,8]
x = 3
output = binarySearch(array, x)
print(f"{x} is found at {output} in the given array")
