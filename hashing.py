class Solution:
    def repeatedCharacter(self, s: str) -> str:
        for i in range(len(s)):
            c = s[i]
            for j in range(i):
                if s[j] == c:
                    return c
        return ""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mappy = {}
        for i in range(len(nums)):
            num = nums[i]
            compl = target - num
            if compl in mappy:
                return [i, mappy[compl]]
            mappy[num] = i
        
        return [-1, -1]