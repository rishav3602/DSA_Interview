## Remove duplicates from an array 

#METHOD-1  --- using function

array = [1,2,3,4,1,2,3,1,2,3,4,6,8,9]
array = set(array)
print(list(array))


#METHOD-2  --- interview types

def drop_duplicates(arr):
    unique_arr = []
    for elements in arr:
        if elements not in unique_arr:
            unique_arr.append(elements)
    return unique_arr

array = [1,2,3,4,1,2,3,1,2,3,4,6,8,9]
output = drop_duplicates(array)
print(f"Your array with unique elements is : {output}")