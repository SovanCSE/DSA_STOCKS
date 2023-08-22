###########################################################################################
##
## Category: Dynamic String Programming
## Title: Leetcode - 5 - Longest palindrome substring in python
## Short notes:
## Time complexity: O(n^2)
## Youtube Link: https://www.youtube.com/watch?v=XYQecbcd6_c&t=5s
## Example1: Input: ababd || Output: aba 
## Example2: Input: dccb  || Output: cc
############################################################################################


def find_longest_palindrome_substring(input_str: str) -> str:
    palindrome_str = ''
    palindrome_str_len = 0
    input_str_length = len(input_str)
    for i in range(input_str_length):
        l,r = i, i+1 if input_str_length%2 == 0 else i
        while l >= 0 and r < input_str_length and input_str[l] == input_str[r]:
            if (r-l+1) > palindrome_str_len: ## if you want to last palindrome substrting while lengh equal the replace > to >=
                palindrome_str = input_str[l:r+1]
                palindrome_str_len = r-l+1
            l -= 1
            r += 1
    return palindrome_str
  
find_longest_palindrome_substring('dccb') ##output: cc
