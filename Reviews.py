class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mappy = {}
        for i in range(len(nums)):
            snum= target- nums[i]
            if snum in mappy:
                return[mappy[snum],i]
            mappy[nums[i]]=i
        return []