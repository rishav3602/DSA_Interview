## remove duplicated from a given array

def drop_duplicates(arr):
    unique_arr = list()
    for i in arr:
        if i not in unique_arr:
            unique_arr.append(i)
    
    return unique_arr



array = [1,2,3,4,4,3,2,1,8,5,8,2,4]
output = drop_duplicates(array)
print(f"The list of array with unique values is : {output}")

print(list(set(array)))

