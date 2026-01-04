nums = [10, 11, 15, 7, 5, 18, 30, 10]
target = 20

seen = {}

for i, num in enumerate(nums):
    missing = target - num

    if missing in seen:
        print([seen[missing], i])
        break

    seen[num] = i
