#################################################################################
## Category: Dynamic Programming
## Title: Chekc if given array is valid mountain array
## Time complexity is O(N)
## Space complexity is O(1)
## Short notes -
##  Length of the array should consist at least 4 elements
##  Checking if array of element intially in creasing and followed by decreasing order
## Example: Input: [0,2,3,4,5,2,1] Ouput: True
## Example: Input: [2, 1, 3] Output: False
##################################################################################

def check_if_valid_mountain_array(array_items):
  
  i = 1
  ## Checking if increasing order
  while (i < len(array_items) and array_items[i] > array_items[i-1]):
    i += 1
  
  #Checking if no more item to iterate further or length of array less than 1
  if i == 1 or i == len(array_items):
    return False

  ## Checking if decreasing order
  while(i < len(array_items) and array_items[i] < array_items[i-1]):
    i+= 1

  return i == len(array_items)

array_items = [1,2, 3,1]
check_if_valid_mountain_array(array_items)
