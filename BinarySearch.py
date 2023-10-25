# Recursive Binary Search: Base Case
# Binary search is an efficient algorithm for finding values in a sorted data-set.

# Let’s implement this algorithm in Python!

# Here’s a recap of the algorithm:

# Check the middle value of the dataset.
# If this value matches our target we return the target value index.
# If the middle value is greater than our target
# Begin at step 1 using the left half of the list.
# If the middle value is less than our target
# Begin at step 1 using the right half of the list.
# As an added challenge, we are going to use a recursive approach. When using recursion, we always want to think of the problem in two ways: the base case and the recursive step.

# We have two base cases for this algorithm:

# We found the value and return its index
# We didn’t find the value because the list is empty!
# In order to reach the base case of an empty list, we’ll need to remove an element at each recursive call…

# A list of the ingredients for tuna sushi
recipe = ["nori", "tuna", "soy sauce", "sushi rice", "avocado"]
target_ingredient = "avocado"

def linear_search(search_list, target_value):
  for idx in range(len(search_list)):
    if search_list[idx] == target_value:
      return idx
  raise ValueError("{0} not in list".format(target_value))

print(linear_search(recipe, target_ingredient))