## reversing an array with different techniques

##METHOD-1 -- using reverse function

def reverse(arr):
    arr = arr[: : -1]
    return arr

array = [1,2,3,4,5]
output = reverse(array)
print(f"Your reversed array is : {output}")

## METHOD-2 -- using swapping technique 

def rev_arr(arr):
    start = 0
    end = len(arr) -1
    while start < end :
        arr[start] , arr[end] = arr[end] , arr[start]
        start += 1
        end -= 1
        
    return arr

array = [1,2,3,4,5,6]
output = rev_arr(array)
print(f"Your sorted array is :{output} ")
