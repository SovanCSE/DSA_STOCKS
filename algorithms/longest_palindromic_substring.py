#################################################################################################################################
## Category: String dynamic Programing
## Title: Find longest palindromic substring
## Short notes -
##  O(n^2) -> Need to see left and right pointer for each of the character to check if find any palindromic substring
## Youtube Link: https://www.youtube.com/watch?v=XYQecbcd6_c&list=PLot-Xpze53leF0FeHz2X0aG3zd0mr1AW_&index=17&ab_channel=NeetCode
##  Example: Input: abbc Output: bb lengh of 2 || Input: babad Output: bab or aba anyone is right
##################################################################################################################################

word = 'babad'
res_word = ''
res_len = 0

for i in range(len(word)):
    left_pointer = i
    right_pointer = i if len(word) % 2 else i+1  # if length of the string is odd number then keep i else i+1
    while left_pointer >= 0 and right_pointer < len(word) and word[left_pointer] == word[right_pointer]:
        if (right_pointer - left_pointer + 1) > res_len:
            res_word = word[left_pointer: right_pointer+1]
            res_len = len(res_word)
        right_pointer += 1
        left_pointer -= 1

print(f"Longest Palindromic substring : {res_word}")
print(f"Length of the longest palindromic substring: {res_len}")




