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
class Solution:
    def romanToInt(self, s: str) -> int:
        mappy={ 'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        tot=0
        for i in range(len(s)):
            if s[i-1]=='I' and s[i] in ['V','X'] and i !=0:
                tot=tot-2+mappy[s[i]]
            elif s[i-1]=='X' and s[i] in ['L','C']and i !=0:
                tot=tot-20+mappy[s[i]]   
            elif s[i-1]=='C' and s[i] in ['D','M']and i !=0:
                tot=tot-200+mappy[s[i]]       
            else:
                tot+=mappy[s[i]]
        return tot