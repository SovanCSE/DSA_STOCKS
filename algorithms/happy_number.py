#################################################################################################################################
## Category: Dynamic programing
## Title: Check If number is happy number
## Short notes -
##  O(n) -> Need to calculate sum of the squares of its digits until equal to 1 or end the loop
## Youtube Link: https://www.youtube.com/watch?v=ljz85bxOYJ0&list=PLot-Xpze53leF0FeHz2X0aG3zd0mr1AW_&index=17&ab_channel=NeetCode
## Example: 
##Input: 19
##Output: True # 19 is a happy number: 1^2 + 9^2 = 82, 8^2 + 2^2 = 68, 6^2 + 8^2 = 100, 1^2 + 0^2 + 0^2 = 1
##Input: 18
##Output: False  # 18 is not a happy number: 1^2 + 8^2 = 65, 6^2 + 5^2 = 61, 6^2 + 1^2 = 37, 3^2 + 7^2 = 58, 5^2 + 8^2 = 89, 8^2 + 9^2 = 145, 1^2 + 4^2 + 5^2 = 42, 4^2 + 2^2 = 20, 2^2 + 0^2 = 4, 4^2 = 16 and 1^2 + 6^2 = 37 which enters a cycle without reaching 1.
##################################################################################################################################

def is_happy_number(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1

# Example usage
print(is_happy_number(19))  # Output: True
print(is_happy_number(18))  # Output: False









