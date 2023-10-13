#################################################################################
## Category: Dynamic Programming
## Title: Find largest subarray and sum of the elements equal to target element k.
## Short Notes -
##  O(N) -   Using starting and end pointer 0 and adding one by one by increasing starting point to get max lengh of array
# Youtube Link: https://www.youtube.com/watch?v=TfQPoaRDeMQ&ab_channel=AdityaVerma
## Example: LIST: [1, -2, -2, 3, 1, 7, 5] sum_values = 1 index_range = [1,5]
## Example: LIST: [1, 2, 3, 7, 5] sum_values = 12 index_range = [2,4]
##################################################################################

def largest_subarray_sum(nums, target):
    
    i = j = array_max_length = sum_values = 0
    index_range = -1
    
    while j < len(nums):
        
        sum_values += nums[j]
        
        #While total sum value crossing the target sum
        while sum_values > target:
            sum_values -= nums[i]
            i += 1
            
        #if finds matching sum with largest subarray
        if sum_values == target and (j-i) + 1 > array_max_length:
            array_max_length = (j-i) + 1
            index_range = [i, j]
            
        #Move forward to next element if total sum less than or equal to target
        j += 1

    if index_range == -1:
        return []
    
    return nums[index_range[0]:index_range[1]+1]

largest_subarray_sum([1, 2, 3, 4, 5], 9) #[2, 3, 4]
largest_subarray_sum([4, 3, 2, 1, 5], 5) #[3, 2]
