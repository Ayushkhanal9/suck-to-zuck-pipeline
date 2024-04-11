# we make a dictionary and then fill it with the key value and the amount of time it appears
# if the count is more than n/2 we return the value as the output
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mappy={}
        for i in range(len(nums)):
            if nums[i] not in mappy:
                mappy[nums[i]]=1
            elif nums[i] in mappy:
                mappy[nums[i]]+=1
        return max(mappy,key=mappy.get)