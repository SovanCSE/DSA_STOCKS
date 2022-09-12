#############################################################################################
## Category: Dynamic Programming
## Title: Find the combination of three numbers which sum up equal to zero
## Short notes -
##  - Initially, need to sort the item list
##  - First interation to find the first elements of sum three combinations
##  - Second loop to find second and third elements of sum three combinations
##  - Third loop to find further second and third elements of sum three combinations if still second left element same increment by one
## Example: Input: [-3, 3, 4, -3, 1, 2] Output: [ [-3, 1, 2] ]
## Example: Input: [-1, 0, 1, 2, -1, -4] Output: [ [-1, 0, 1] , [-1, -1, 2] ]
##############################################################################################

nums = [-1, 0, 1, 2, -1, -4]
nums.sort()
res = list()
for i, num in enumerate(nums):
    if i > 0 and nums[i] == nums[i-1]:
        continue
    left_pointer, right_pointer = i+1, len(nums) - 1
    while left_pointer < right_pointer:
        three_sum = num + nums[left_pointer] + nums[right_pointer]
        if three_sum > 0:
            right_pointer -= 1
        elif three_sum < 0:
            left_pointer += 1
        else:
            res.append([num, nums[left_pointer], nums[right_pointer]])
            left_pointer += 1
            while nums[left_pointer] == nums[left_pointer-1] and left_pointer < right_pointer:
                left_pointer += 1
print(f"Result set O(N^3) {res}")