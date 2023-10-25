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



# define binary_search()
def binary_search(sorted_list, target):
  if not sorted_list:
    return 'value not found'
  mid_idx = len(sorted_list)//2
  mid_val = sorted_list[mid_idx]
  if mid_val == target:
    return mid_idx

# INARY SEARCH: PYTHON
# Recursive Binary Search: Base Case 2
# We now have a base case for when we do not find the value in our sorted list, but we need a base case for when we DO find the value.

# At this step, we have three options:

# BASE CASE: mid_val matches our target
# RECURSIVE STEP: mid_val is less than our target
# RECURSIVE STEP: mid_val is more than our target
# We’ll tackle the alternate base case first.

# Instructions
# Checkpoint 1 Passed
# 1.
# Let’s complete the base case for when we have found the value.

# After the declarations for mid_val and mid_idx, write a conditional that checks if mid_val is our target.

# If it is, return mid_idx.

# For testing:
sorted_values = [13, 14, 15, 16, 17]
print(binary_search([], 42))
print(binary_search(sorted_values, 42))
print(binary_search(sorted_values, 15))




# define binary_search()
def binary_search(sorted_list, target):
  if not sorted_list:
    return 'value not found'
  mid_idx = len(sorted_list)//2
  mid_val = sorted_list[mid_idx]
  if mid_val == target:
    return mid_idx
  elif mid_val > target:
    left_half = sorted_list[: mid_idx]
    return binary_search(left_half, target)
  elif mid_val < target:
    right_half = sorted_list[mid_idx+1:]
    result = binary_search (right_half, target)
    if result == "value not found":
      return result
    else:
      return result + mid_idx + 1
    

# For testing:
sorted_values = [13, 14, 15, 16, 17]
print(binary_search(sorted_values, 16))