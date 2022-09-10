#######################################################################################################################
## Category: Dynamic Programming
## Title: Give list of numbers, find the indices of the two numbers which sum up to a specific target number
## Short notes -
##   O(N^2) -  iterate one of one element starting from end if end element crossing sum than target than reduce the list from right slide
##   O(N) - Use two pointer one at left and other at right end then keep decreasing and increasing depends on the sum value
## Example: input: [1, 3, 4, 5, 7, 10, 11] target = 9 Output: [3,4]
############################################################################################################################

## Solution with brute force time complexity O(N^2)
input_numbers = [1, 3, 4, 5, 7, 10, 11]
sum_target = 9
found_sum = False
for i in range(len(input_numbers)):
    for j in range(i+1, len(input_numbers)):
        if (input_numbers[i] + input_numbers[j]) == sum_target:
            found_sum = True
            break
        elif (input_numbers[i] + input_numbers[j]) > sum_target:
            input_numbers = input_numbers[:j]
            break
    if found_sum:
        print(f'Result indices O(N^2) [{i+1} , {j+1}]')
        break
else:
    print("not found indices for numbers with the specific target sum O(N^2)")


## Solution with linear time complexity O(N)

i = 0
j = len(input_numbers) - 1

while i < j:
    if (input_numbers[i] + input_numbers[j]) > sum_target:
        j -= 1
    elif (input_numbers[i] + input_numbers[j]) < sum_target:
        i += 1
    else:
        print(f'Result indices O(N) [{i+1} , {j+1}]')
        break
else:
    print("not found indices for numbers with the specific target sum O(N)")


