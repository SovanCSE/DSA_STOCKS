#################################################################################
## Category: Matrix
## Title: Write an efficient program which searehes for a value in an  m * n matrix. This matrix has the following properties -
##   1. Integers in each row sorted from left to right
##   2. The first integer of each row is greater than last integer of the previous row
## Short notes -
##  O(Log M + Log N) - First step finding the row which having the target element using binary search.
##                   - Second step finding the target element in specific row using binary search.
## Youtube link: https://www.youtube.com/watch?v=Ber2pi2C0j0&list=PLot-Xpze53leF0FeHz2X0aG3zd0mr1AW_&index=5&ab_channel=NeetCode
## Example:
## Input Matrix: [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]] target = 3
## Output: True
##################################################################################

matrix_values = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
row_length = len(matrix_values)
col_length = len(matrix_values[0])
starting_row, ending_row = 0, row_length -1

while starting_row <= ending_row:
    mid_row = (starting_row + ending_row) // 2
    #Checking the target greater than last integer of the current row
    if target > matrix_values[mid_row][-1]:
        starting_row = mid_row + 1
    #Checking if target less than the first integer of the current row
    elif target < matrix_values[mid_row][0]: 
        ending_row = mid_row - 1
    else:
        break
if not (starting_row <= ending_row):
    print(False)
else:
    selected_row = (starting_row + ending_row) // 2
    left_pointer, right_pointer = 0, col_length
    while left_pointer <= right_pointer:
        mid_pointer = (left_pointer + right_pointer) // 2
        if target > matrix_values[selected_row][mid_pointer]:
            left_pointer = mid_pointer + 1
        elif target < matrix_values[selected_row][mid_pointer]:
            right_pointer = mid_pointer - 1
        else:
            # print(f'Index position [{selected_row}, {mid_pointer}]')
            print(True)
            break
    else:
        print(False)




