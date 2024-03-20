class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mappy = {}
        for i in range(len(nums)):
            snum= target- nums[i]
            if snum in mappy:
                return[mappy[snum],i]
            mappy[nums[i]]=i
        return []
class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        left = 0
        right = len(num)-1
        is_true= True
        while left<right:
            if num[left]!=num[right]:
                return False
            left+=1
            right-=1
        return True