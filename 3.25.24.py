class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mappy={}
        for i in range(len(nums)):
            if nums[i] in mappy:
                mappy[nums[i]]+=1
                print(mappy)
            else:
                mappy[nums[i]]=1
                print(mappy)
            if mappy[nums[i]]>(len(nums)//2):
                print(mappy)
                return(nums[i])
        return max(mappy,key=mappy.get)