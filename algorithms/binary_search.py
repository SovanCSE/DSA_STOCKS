###########################################################################################
##
## Category: Dynamic Programming
## Title: Find element in sorted list using binary search
## Short notes:
##  O(long n) ->(Average Case) -> using divide and consuer technique on sorted listed
##  O(1) -> (Best Case) ->  using divide and consuer technique on sorted listed
## Youtube Link:
## Example: Input: items: [7, 9, 11, 23] find_item = 11 Output: 3
############################################################################################


def binary_search(nums, target):
    left_pointer = 0
    right_pointer = len(nums)
    while left_pointer <= right_pointer:
        mid_point = (left_pointer+right_pointer)//2
        if nums[mid_point] == target:
            return mid_point
        elif target > nums[mid_point]:
            left_pointer = mid_point + 1
        else:
            right_pointer = mid_point - 1
    return -1
        
binary_search([1, 3, 5, 7, 9, 11], 7) # Output: 3
binary_search([2, 4, 6, 8, 10], 5) #Output: -1
