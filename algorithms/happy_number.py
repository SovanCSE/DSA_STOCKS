#################################################################################################################################
## Category: Dynamic programing
## Title: Check If number is happy number
## Short notes -
##  O(n) -> Need to calculate sum of the squares of its digits until equal to 1 or end the loop
## Youtube Link: https://www.youtube.com/watch?v=ljz85bxOYJ0&list=PLot-Xpze53leF0FeHz2X0aG3zd0mr1AW_&index=17&ab_channel=NeetCode
## Example: Input: 19  Output: True || Input: 2 Output: False
##################################################################################################################################

digits = 19
set_values = set()


def sum_of_square_digits(number):
    output = 0

    while number:
        reminder = number % 10
        output += reminder ** 2
        number = number // 10
    return output


num = sum_of_square_digits(digits)
while num not in set_values:
    set_values.add(num)
    num = sum_of_square_digits(num)

    if num == 1:
        print(f'{digits} is happy number')
        break
else:
    print(f'{digits} is not happy number')








