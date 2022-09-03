#################################################################################
## Youtube Link: https://www.youtube.com/watch?v=TfQPoaRDeMQ&ab_channel=AdityaVerma
## FIND LARGEST SUBARRAY OF sum_values K
## Example: LIST: [1, -2, -2, 3, 1, 7, 5] sum_values = 1 index_range = [1,5]
## Example: LIST: [1, 2, 3, 7, 5] sum_values = 12 index_range = [2,4]
##################################################################################

# arr = [1, -2, -2, 3, 1, 7, 5]
arr = [1, 2, 3, 7, 5]
k = 12
i = j = array_max_length = sum_values = 0
index_range = [-1]
while j < len(arr):
    sum_values += arr[j]
    #While total sum value crossing the target sum
    while sum_values > k:
        sum_values -= arr[i]
        i += 1
    #if finds matching sum with largest subarray
    if sum_values == k and (j-i) + 1 > array_max_length:
        array_max_length = (j-i) + 1
        index_range = [i+1, j+1]
    #Move forward to next element if total sum less than or equal to target
    j += 1
print(f"MAX LENGTH: {array_max_length}, INDEX RANGE:  {index_range}")