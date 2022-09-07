#################################################################################
## Category:  Dynamic Programming
## Title: Find the longest substring in string without repeating characters
## Short notes -
##    O(N^2) - Using starting pointer to initialize at the start point for further deletes and move forward once get duplicates and other pointer to iterate one ny one elemnent
## Youtube Link: https://www.youtube.com/watch?v=wiGpQwVHdE0&ab_channel=NeetCode
# Example: Input: abcabcbb Output: 3
# Explanation: The answer is abc with length of 3
##################################################################################

word = 'abcabdftab'
store_char = list()
starting_pointer = 0
max_length = 0
max_str = word[0]
for indx, ch in enumerate(word):
    while ch in store_char:
        store_char.remove(word[starting_pointer])
        starting_pointer += 1
    store_char.append(ch)
    if len(store_char) > max_length:
        max_length = len(store_char)
        max_str = ''.join(store_char)
print(f"max_length {max_length} and longest substring is {max_str}")

