#################################################################################
## Category: Dynamic Programming
## Tile: Given num of elements and sort in-place in ascending order
## Short Notes: Using Quick sort partition logic here (Need three pointer here)
##   O(N) - Using three pointers here like left to store zeros, right to store twos and third pointer to check and  swap values left and right.
##      - Remerber third pointer not to increment while get value 2 and swapping with right pointer position
## Youtube Link: https://www.youtube.com/watch?v=4xbWSRZHqac&list=PLot-Xpze53leF0FeHz2X0aG3zd0mr1AW_&index=6&ab_channel=NeetCode
## Example: Input: [2, 0, 2, 1 , 1, 0] Output: [0, 0, 1, 1, 2, 2]
##################################################################################

num_list = [2, 0, 2, 1 , 1, 0]
left_pointer = 0
right_pointer = len(num_list) - 1
dynamic_pointer = 0
while dynamic_pointer <= right_pointer:
    if num_list[dynamic_pointer] == 0:
        num_list[dynamic_pointer], num_list[left_pointer] = num_list[left_pointer], num_list[dynamic_pointer]
        left_pointer += 1
    elif num_list[dynamic_pointer] == 2:
        num_list[dynamic_pointer], num_list[right_pointer] = num_list[right_pointer], num_list[dynamic_pointer]
        right_pointer -= 1
        dynamic_pointer -= 1
    dynamic_pointer += 1
print('Sorted list', num_list)

