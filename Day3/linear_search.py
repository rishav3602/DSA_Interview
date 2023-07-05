## search the given element from the array

def lnr_srch(arr , x):
    for i in range (len(arr)):
        if arr[i] == x:
            return i
    
    return -1
        
array = [1,2,3,4,5,6,7,8]
n = 6
output = lnr_srch(array , n)
print(f"{n} is found at {output} ")