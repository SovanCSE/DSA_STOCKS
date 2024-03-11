#################################################################################
## Category: Dynamic Programming
## Title: Count no. of boats to save people
## Time complexity is O(N log(N))
## Space complexity is O(N)
## Short notes -
##  First stage need to sort the arrya in ascedning order
##  the weights of people left and right side less than or equal to the limit then put in the boat.
## Then increase left end decrease right end by one.
## Example: Input: [1,2,3,3] Ouput: 3
## Example: Input: [1,1,1,1] Output: 2
##################################################################################


def no_of_boats_to_save_people(people_weight, weight_limit):
  people_weight.sort()
  light_weight = 0
  heavy_weight = len(people_weight) - 1
  boats = 0

  while heavy_weight >= light_weight:
    if people_weight[heavy_weight] + people_weight[light_weight] <= weight_limit:
      boats += 1
      heavy_weight -= 1
      light_weight += 1
    else:
      boats += 1
      heavy_weight -= 1
  return boats

people_weight = [1,1,1,1]
weight_limit = 4
no_of_boats_to_save_people(people_weight, weight_limit)
