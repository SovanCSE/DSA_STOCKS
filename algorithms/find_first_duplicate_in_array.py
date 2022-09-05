#################################################################################
## Category: Dynamic Programming
## Title: Find first duplicate element in list of elements
## Short notes -
##   O(N^2) - Use two loop  to find second duplicate position one ny one the elements.
##   O(N) - Use hash set to store and compare duplicate to find first duplicate element
# Youtube Link: https://www.youtube.com/watch?v=XSdr_O-XVRQ&ab_channel=NickWhite
## Example: Input: [1, 2, 1, 2, 3, 3] Ouput: 1
## Example: Input: [2, 1, 3, 5, 3, 2] Output: 3
## Example: [1, 2, 3, 4, 5] Output: -1
##################################################################################

## Solution with time complexity O(N^2)
items = [2, 1, 3, 5, 3, 2]
index_value_of_second_duplicates = len(items)
for i in range(len(items)):
    for j in range(i+1, len(items)):
        if items[i] == items[j]:
            index_value_of_second_duplicates = min(index_value_of_second_duplicates, j)
if index_value_of_second_duplicates == len(items):
    print('No duplicate elements O(N^2):: ', -1)
else:
    print('First duplicate value is O(N^2):: ', items[index_value_of_second_duplicates])

## Solution with time complexity O(N)
hash_set = set()
find_duplicates = False
for item in items:
    if item in hash_set:
        find_duplicates = True
        print('First duplicate value is O(N):: ', item)
        break
    else:
        hash_set.add(item)
if not find_duplicates:
    print('No duplicate elements O(N):: ', -1)

