#porgram that gives us the key with the biggest value. technically it just the number that appears n/2 times but because majority elem is always present we can technically just return
# the key with biggest value
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mappy={}
        for i in range(len(nums)):
            if nums[i] not in mappy:
                mappy[nums[i]]=1
            elif nums[i] in mappy:
                mappy[nums[i]]+=1
        return max(mappy, key=mappy.get)