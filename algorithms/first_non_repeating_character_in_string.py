#################################################################################
## YouTube link: https://www.youtube.com/watch?v=5co5Gvp_-S0&ab_channel=NickWhite
## Input type - String
## Input string contains only lower case english letters so cann't be "" or "B23D"
## Input string length - 1  <= N <= 100000
## Example input: aaabccc ouptput: b
## Example input: abcbad output: c
## Example input: aaabcccdeef ouput: b
## Example output: abcabcac outout: _ (all characters are repeating here)
##################################################################################

## SCRIPT LOGIC WITH O(N^2) TIME COMPLEXITY
str = 'aaabcccdeef'
n = len(str)
find_duplicate = False
for i in range(n):
    find_duplicate = False
    for j in range(n):
        if str[i] == str[j] and i != j:
            find_duplicate = True
            break
    if not find_duplicate:
        print('First occurrence character O(n^2): ', str[i])
        break
if find_duplicate:
    print('There are no unique character O(n^2): _')


# OPTION 1: SCRIPT LOGIC WITH O(N) TIME COMPLEXITY - with find() and rfind()  methods
has_duplicate = True
for chr in str:
    if str.find(chr) == str.rfind(chr):
        has_duplicate = False
        print('First occurrence character O(n): ', chr)
        break
if has_duplicate:
    print('There are no unique character O(n): _')

# OPTION 2: SCRIPT LOGIC WITH O(N) TIME COMPLEXITY - orderedDict get and put operator time complexity is 1

from collections import OrderedDict

custom_dict = OrderedDict()
for chr in str:
    if chr in custom_dict:
        custom_dict[chr] += 1
    else:
        custom_dict[chr] = 1

for key, val in custom_dict.items():
    if val == 1:
        print('First occurrence character O(n): ', key)
        break
else:
    print('There are no unique character O(n): _')