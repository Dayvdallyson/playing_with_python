nums = [3, 1, 5, 7]
target = 8

for num in nums:
    for num2 in nums:
        if num + num2 == target:
            print(nums.index(num), nums.index(num2))
