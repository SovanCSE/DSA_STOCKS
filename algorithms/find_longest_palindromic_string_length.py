###########################################################################################
##
## Category: Dynamic String Programming
## Title: Leetcode - 409 - Longest palindrome length in python
## Short notes:
## Time complexity: O(n)
## Youtube Link: https://www.youtube.com/watch?v=ci4PIq1NWoU&t=195s
## Example1: Input: abccccddd || Output: 7
############################################################################################

def longest_palindrome_length(input_str: str) -> str:
    letters = {}
    for char in input_str:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    
    max_palindrome_length = 0
    odd_char_count = 0
    
    if len(letters) == 1:
        return letters[input_str[0]]
        
    for char_count in letters.values():
        if char_count > 1:
            if char_count%2 == 0:
                max_palindrome_length += char_count
            else:
                max_palindrome_length += char_count - 1
                odd_char_count += 1
        else:
            odd_char_count += 1
    if odd_char_count > 0:
        max_palindrome_length += 1
    return max_palindrome_length  
        
longest_palindrome_length('abccccddd') ## output: 7
