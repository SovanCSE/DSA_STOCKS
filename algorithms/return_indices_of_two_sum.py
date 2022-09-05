#################################################################################
## Category:  Dynamic Programming
## Title: Given an array of integrers, return indices of the two numbers such that they add up to the specific target.
## Short notes -
##    O(N^2) - using two loop we can find the two elements come to the target sum
##    O(N) - Storing value as key and index as value in dictionary and checking if (target - current element) present in dict key then returning the both indices
## Example: Input: [2, 7, 11, 5] target: 9 Output: [0,1] if don't find it should return empty list
##################################################################################

# Solution with time complexity O(N^2)
input_array = [2, 7, 11, 5]
target = 9
i = 0
j = 0
result_index = []
for i in range(len(input_array)):
    for j in range(i+1, len(input_array)):
        if input_array[i] + input_array[j] == target:
            result_index.append([i, j])
print(f"result_index O(N^2):: {result_index}")


#Solution with time complexity O(N)
lookup = {}
result_index = []
for indx, val in enumerate(input_array):
    if target - val in lookup:
        result_index.append([lookup[target-val], indx])
    lookup[val] = indx
print(f"result_index O(N):: {result_index}")

