###########################################################################################
##
## Category: Dynamic Programming
## Title: Sort elements in list using quicksort algorithm
## Short notes:
##  O(n long n) ->(Best Case) -> Considering first element as pivot and placing it to right position according sort order,
##                   follow the same for other partition recursively to get the whole list as sorted
##  O(n^2) -> (Worse Case)
## Youtube Link: https://www.youtube.com/watch?v=UA_Rmjfj4bw&ab_channel=AnujBhaiya
## Example: Input: [4, 6, 2, 5, 7, 9, 1, 3] Output: [1, 2, 3, 4, 5, 6, 7, 9]
############################################################################################


def partition(left_pointer, right_pointer):
    pivot = items[left_pointer]
    i = left_pointer
    j = right_pointer

    while i < j:
        while items[i] <= pivot:
            i += 1
        while items[j] > pivot:
            j -= 1
        if i < j:
            items[i], items[j] = items[j], items[i]
    items[j], items[left_pointer] = items[left_pointer], items[j]
    return j


def quicksort(left_pointer, right_pointer):
    if left_pointer < right_pointer:
        pivot = partition(left_pointer, right_pointer)
        quicksort(left_pointer, pivot-1)
        quicksort(pivot + 1, right_pointer)


items = [4, 6, 2, 5, 7, 9, 1, 3]
left_pointer = 0
right_pointer = len(items) - 1
quicksort(left_pointer, right_pointer)
print('sorted item', items)