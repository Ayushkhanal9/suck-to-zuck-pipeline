# #contains duplicate II
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in 
#the array such that nums[i] == nums[j] and abs(i - j) <= k.

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    mappy={}
    hasduplicate=False
    for i in range(len(nums)):
        if nums[i] not in mappy:
            mappy[nums[i]]=i
        elif nums[i] in mappy:
            if i-mappy[nums[i]] <= k:
                hasduplicate=True
            mappy[nums[i]]=i
    return hasduplicate