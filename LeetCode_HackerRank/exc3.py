def twoSum(nums, target):
    for i, j in enumerate(range(0, len(nums))):
        if (nums[i] + nums[j]) == target:
            return target
    return -1

nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))