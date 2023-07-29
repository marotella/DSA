# define your linear_search() below...
def linear_search(search_list, target_value):
  for index in range(len(search_list)):
    print(search_list[index])
    if search_list[index] == target_value:
      return index
  raise ValueError("{target_value} is not in the list")

# uncomment the lines below to test...
values = [54, 22, 46, 99]
print(linear_search(values, 22))



def linear_search(search_list, target_value):
  for idx in range(len(search_list)):
    if search_list[idx] == target_value:
      return idx
  raise ValueError("{0} not in list".format(target_value))



try:
  # Call the function below...
  result = linear_search(number_list, target_number)
  print(result)
  linear_search(number_list, 100)
except ValueError as error_message:
  print("{0}".format(error_message))