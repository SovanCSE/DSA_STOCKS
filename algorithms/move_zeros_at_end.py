#################################################################################
## Category: Dynamic Programming
## Title: Move Zeros
## Time complexity is O(N)
## Space complexity is O(1)
## Short notes -
##  Use one pointer to store all non-zero values beginning of the array
##  Next replace rest of the array fill with zeros
## Example: Input: [0, 1, 0, 3, 12, 15,0] Ouput: [1, 3, 12, 15, 0, 0, 0]
## Example: Input: [0, 1, 0, 3, 12] Output:  [1, 3, 12, 0, 0]
################################################################################

def move_zeros_at_end(items):
  pointer_index = 0
  n = len(items)

  ## Initially storing all non-zero elements at beginning of the array
  for array_index in range(0, n):
    if items[array_index] != 0:
      items[pointer_index] = items[array_index]
      pointer_index += 1

  ## Reamining rest of array are filling with zeros
  for inx in range(pointer_index, n):
    items[inx] = 0
  return items

items = [0, 1, 0, 3, 12, 15,0]
new_items = move_zeros_at_end(items)
print(new_items)
