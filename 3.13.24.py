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

#Guess number higher or lower
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

def guessNumber(n: int) -> int:
    left=0
    right = n
    while True:
        mid=left+(right-left)//2
        result=guess(mid)
        if result > 0:
            left=mid+1
        elif result <0:
            right=mid-1
        else:
            return mid
    return -1
#search insert positions. We use binary search method to do this
def searchInsert(nums: List[int], target: int) -> int:
    low = 0
    high= len(nums)-1
    while low <= high:
        mid = low+(high-low)//2
        if target<nums[mid]:
            high = mid-1
        elif target > nums[mid] :
            low= mid+1
        else:
            return mid
    return low