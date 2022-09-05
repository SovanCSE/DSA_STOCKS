#################################################################################
## Category: Dynamic Programming
## Title: Find first and last index position of the target element in a sorted array using time complexity O(log N)
## Short Notes :
##   Using the binary searcch algorithm ->  target_item <= list_items[midpoint] to find start index as midpoint
##     and target_item >= list_items[midpoint] to find end index as midpoint.
## Youtube Link: https://www.youtube.com/watch?v=bU-q1OJ0KWw&ab_channel=NickWhite
## Example: input: list_items = [5, 7, 7, 8, 8, 10] target_item = 8 Output: [3,4]
## Example: input: list_items = [5, 7, 7, 8, 8, 10] target_item = 3 Output: [-1, -1]
##################################################################################

#Solution with time complexity O(log N)
def find_start_index(list_items, target_item):
    start_point = 0
    end_point = len(list_items)
    index_value = -1
    while start_point <= end_point:
        midpoint = (end_point + start_point)//2
        #get the minimum index value of the target_item item
        if target_item <= list_items[midpoint]:
            end_point = midpoint - 1
        else:
            start_point = midpoint + 1
        if target_item == list_items[midpoint]:
            index_value = midpoint
    return index_value


def find_end_index(list_items, target_item):
    start_point = 0
    end_point = len(list_items)
    index_value = -1
    while start_point <= end_point:
        midpoint = (end_point + start_point) // 2
        # get the maximum index value of the target_item item
        if target_item >= list_items[midpoint]:
            start_point = midpoint + 1
        else:
            end_point = midpoint - 1
        if target_item == list_items[midpoint]:
            index_value = midpoint
    return index_value


if __name__ == "__main__":
    list_items = [5, 7, 7, 8, 8, 10]
    target_item = 8
    start_index = find_start_index(list_items, target_item)
    end_index = find_end_index(list_items, target_item)
    result = [start_index, end_index]
    print(f'First and last position of element {target_item} and position are {result}')
