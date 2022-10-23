###########################################################################################
##
## Category: Dynamic Programming
## Title: Find element in list using linear search
## Short notes:
##  O(n^) ->(Average Case) -> find itme by iterating one by one element
##  O(1) -> (Best Case) ->  find itme by iterating one by one element
## Youtube Link:
## Example: Input: items: [ 9, 7, 11, 10] find_item = 11 Output: 3
############################################################################################


items = [9, 7, 11, 10]
find_item = 11
for i in range(len(items)):
    if find_item == items[i]:
        print(f"Find element position at  {i + 1}")
        break
else:
    print('Unable to find item in list')

