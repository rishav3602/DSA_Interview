## Find min and max element in an arry

array = [1,2,3,4,5,6,7,8]
print("Minimum is : ",min(array))
print("Maximum is : ",max(array))



def find_min_max(arr):
    min = arr[0]
    max = arr[0]
    if len(arr) == 0:
        return -1
    else:
        for element in arr:
            if element < min:
                min = element
            elif element > max:
                max = element

    return min , max

arr = [1,2,3,4,5,6,7,8,20]
output = find_min_max(arr)
print(f"The minimum and maximum elements of the given array is : {output}")


