################################################################################################################## 
##Category: Dynamic String Programming
## Title: Leetcode - 205 - Isomorphic string in python
## Short notes - Two strings s and t are isomorphic if characters in s can be replaced to get t.
## Restrictions -
## 1. All occurrence of characters must be replaces with another character while preserving the order of characters.
## 2. No two characters may replace to the same character
## 3. But character may map with itself
## Time complexity: O(n)
## Youtube Link: https://www.youtube.com/watch?v=7yF-U1hLEqQ
# Example
# string1 = 'egg' and string2 = 'add' Result=True
# string1 = 'foo' and string2 = 'bar' Result=True
##################################################################################################################

def check_if_two_strings_isomorphic(s,t):
    mapST = mapTS = {}
    for c1, c2 in zip(s,t):
        
        if (c1 in mapST and mapST[c1]!=c2) or (c2 in mapTS and mapTS[c2]!=c1):
            return False
        mapST[c1] = c2
        mapTS[c2] = c1
    return True
check_if_two_strings_isomorphic('egg', 'add') #True
