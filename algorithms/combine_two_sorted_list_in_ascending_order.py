#################################################################################
## Youtube Link: Combine two sorted list and display in the list in ascending order
## Example: input: list1 = [1, 5, 6, 9, 11] and list2 = [3, 4, 7, 8, 10] Output: [1, 3, 4, 5, 6, 7, 8, 9, 10, 11]
##
##################################################################################

# Solution with time complexity O(N^2) called as bubble sort
list1 = [1, 5, 6, 9, 11]
list2 = [3, 4, 7, 8, 10]
new_list = list1 + list2
for i in range(len(new_list)):
    for j in range(len(new_list)-1-i):
        if new_list[j] > new_list[j+1]:
            new_list[j], new_list[j+1] = new_list[j+1], new_list[j]
print('Sorted list O(N^2)::', new_list)


# Solution with time complexity O(N)
i, j = 0, 0
res = []

while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        res.append(list1[i])
        i += 1
    else:
        res.append(list2[j])
        j += 1
res.extend(list1[i:] + list2[j:])
print('Sorted list O(N)::', res)

