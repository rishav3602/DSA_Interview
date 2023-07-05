## reverse an array in plane

arr = [1,2,3,4,5,6,7,8]
print(f"reversed array: {arr[::-1]}")

def rev_arr(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        ## start swapping
        arr[start] , arr[end] = arr[end] , arr[start]
        start += 1
        end -= 1

    return arr

arr = [10, 20 ,30, 40, 50, 60]
output = rev_arr(arr)
print(f"Your reversed array is : {output}")