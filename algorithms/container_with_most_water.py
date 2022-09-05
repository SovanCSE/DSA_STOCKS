#################################################################################
##
## Category: Dynamic Programming
## Title: Find the maximum rectangular area(width * height) to contain the most of the water without overflow
## Short Notes:
##  O(N^2) - Using two loop to iterate between any of two points and find out the max area among of them
##  O(N) ->  Using left and right pointer  to find max area values if right pointer value more then moving the left pointer forward otherwise right pointer.
## Youtube Link: https://www.youtube.com/watch?v=UuiTKBwPgAo&ab_channel=NeetCode
## Example: input: [1, 8, 6, 2, 5, 4, 8, 3, 7] Output: 49 (7*7) where starting index is 1 and end index is 8
##
##################################################################################

## Solution(BRUTE FORCE APPROACH) with time complexity O(N^2)
input_array = [1, 8, 6, 2, 5, 4, 8, 3, 7]
res = 0
for i in range(len(input_array)):
    for j in range(i+1, len(input_array)):
        rec_area = (j-i) * min(input_array[i], input_array[j])
        res = max(rec_area, res)
print(f'Maximum container size O(N^2): {res}')


## Solution(Linear time solution) with time complexity O(N)
res = 0
left_pointer, right_pointer = 0, len(input_array) - 1
max_area = 0

#If left equals to right or left passes the right  both not good either
while left_pointer < right_pointer:
    rec_area = (right_pointer - left_pointer) * min(input_array[left_pointer], input_array[right_pointer])
    res = max(rec_area, res)
    if input_array[right_pointer] > input_array[left_pointer] :
        left_pointer += 1
    else:
        right_pointer -= 1

print(f'Maximum container size O(N): {res}')

