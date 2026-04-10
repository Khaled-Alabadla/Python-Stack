# Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element)
def countDown(num):
  for i in range(num, -1, -1):
    print(i)

countDown(5)

print("===============================")

# Create a function that will receive a list with two numbers. Print the first value and return the second
def print_and_return(nums):
  print(nums[0])
  return nums[1]

result = print_and_return([3, 4])
print(result)

print("===============================")

# Create a function that accepts a list and returns the sum of the first value in the list plus the list's length
def sum(nums):
  return nums[0] + len(nums)

print(sum([1, 2, 3, 4, 5]))

print("===============================")

# Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
def values_greater_than_second(nums):
  result = []

  if(len(nums) < 2):
    return False

  for i in nums:
    if i > nums[1]:
      result.append(i)

  print(len(result))
  return (result if len(result) > 0 else False)

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

print("===============================")

# Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value
def length_and_value(size, value):
  result = []
  for i in range(size):
    result.append(value)
  return result

print(length_and_value(3, 7))


