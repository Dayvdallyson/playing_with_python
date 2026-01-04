# find the indexes of the two numbers that add up to 5

nums  = [1, 2, 3, 4, 5]


for num in nums:
  for num2 in nums:
    if num + num2 == 5:
      print(nums.index(num), nums.index(num2))


