def containsDuplicate(nums):
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    
    return False

def constainsDuplicateNeetCode(nums2):
    hashset = set()

    for i in nums2:
        if i in hashset:
            return True
        hashset.add(i)
    return False

nums2 = [1,2,4,5,2,2,2,3]
print(constainsDuplicateNeetCode(nums2))