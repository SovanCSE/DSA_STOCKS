#################################################################################
## Category: Dynamic Programming
## Title: Find the contiguous subarray with maximum sum
## Short notes -
##   O(N) - Use one starting pointer if get negative value in sum then assign current sum to zero
## Youtube Link: https://www.youtube.com/watch?v=5WZl3MMT0Eg&list=PLot-Xpze53leF0FeHz2X0aG3zd0mr1AW_&index=14&ab_channel=NeetCode
## Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
## Output: 6
## Explanation: [4, -1, 2, 1] has the largest sum 6
##################################################################################

input_nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum = input_nums[0] #list should contains at least one numner
current_sum = 0
starting_index = 0
ending_index = len(input_nums) - 1

for indx, num in enumerate(input_nums):
    if current_sum < 0:
        current_sum = 0
        starting_index = indx
    current_sum += num
    if current_sum > max_sum:
        max_sum = current_sum
        ending_index = indx
print(f'maximum sum = {max_sum} and index range [{starting_index}, {ending_index}]')