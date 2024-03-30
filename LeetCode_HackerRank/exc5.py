def containsDuplicate(nums):
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    
    return False

nums = [1,2,4,5]
print(containsDuplicate(nums))