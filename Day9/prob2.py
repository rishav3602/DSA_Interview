"""
<aside>
💡 **Q2.** Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

- Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
- Return k.

**Example :**
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_*,_*]

**Explanation:** Your function should return k = 2, with the first two elements of nums being 2. It does not matter what you leave beyond the returned k (hence they are underscores)[

</aside>
"""

def remove_val(arr,x):
    rem_ele = list()
    if x in arr:
        for i in arr:
            if i == x:
                rem_ele.append(i)
                count = len(rem_ele)
        return count
    else:
        print("Given element is not present in the given array")
        return None
            
        
        

array = [3,2,2,3,3]
output = remove_val(array,2)
print(output)
