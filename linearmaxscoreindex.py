# Search list
test_scores = [88, 93, 75, 100, 80, 67, 71, 92, 90, 83]

#Linear Search Algorithm
def linear_search(search_list):
  maximum_score_index = None
  for idx in range(len(search_list)):
    if not maximum_score_index or search_list[idx] > search_list[maximum_score_index]:
      maximum_score_index = idx
  return maximum_score_index

# Function call
highest_score = linear_search(test_scores)

#Prints out the highest score in the list
print(highest_score)


# Review
# You are a linear search whiz!

# You have implemented linear search as a function in Python and used it to find a target value, duplicates, and the largest value in different search lists.

# Let’s review what we learned:

# Linear search is a search algorithm that sequentially checks whether a given value is an element of specified list by scanning the elements of a list one-by-one until it finds the target value.

# Starting with linear search as a subroutine in your code is a useful foundation for constructing algorithms to solve more advanced search problems, such as:

# Finding duplicates - sequentially search the list for all occurrences of the target value.
# Finding the maximum value - sequentially scan the list for the largest value and track the largest value seen to date.
# The linear_search() function is provided in the text editor.

# Test on your own examples!

# A list of the ingredients for tuna sushi
recipe = ["nori", "tuna", "soy sauce", "sushi rice", "avocado"]
target_ingredient = "avocado"

def linear_search(search_list, target_value):
  for idx in range(len(search_list)):
    if search_list[idx] == target_value:
      return idx
  raise ValueError("{0} not in list".format(target_value))

print(linear_search(recipe, target_ingredient))