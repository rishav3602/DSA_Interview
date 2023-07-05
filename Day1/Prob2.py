## Find max and min in an array using different functions

## METHOD-1  --- using min and max function

array = [1,2,3,4,5,6]
print(f"Your minimum element is : {min(array)}")
print(f"Your minimum element is : {max(array)}")


## METHOD-2 --- without using min and max function

def min_max(arr):
    min = arr[0]
    max = arr[0]
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
        elif arr[i] > max:
            max = arr[i]
    return min , max

array = [1,2,3,4,5,6]
output = min_max(array)
print(f"The minimum and maximum value in the given array is : {output}")