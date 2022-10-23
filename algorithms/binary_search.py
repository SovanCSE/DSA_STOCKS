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


items = [7, 9, 11, 23]
find_item = 17
left_pointer = 0
right_pointer = len(items)
while left_pointer <= right_pointer:
    mid_point = (left_pointer+right_pointer)//2
    if items[mid_point] == find_item:
        print(f'{find_item} found at position {mid_point+1}')
        break
    elif find_item > items[mid_point]:
        left_pointer = mid_point + 1
    else:
        right_pointer = mid_point - 1
else:
    print('Find item is not present in list of items')
