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
    
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref=''
        sml_str=min(strs,key=len)
        print(sml_str)
        for i in range(len(sml_str)):
            same = True
            for j in range(len(strs)):
                if strs[j][i]!= sml_str[i] :
                    same = False
                    return pref
            if same != False:
                    pref+=sml_str[i]
        return pref
    
class Solution:
    def isValid(self, s: str) -> bool: 
        mappy= {')':'(', '}':'{', ']':'['}
        stack=[]
        if len(s)==1:
            return False
        for i in range(len(s)):
            if s[i] in ['(','{','[']:
                stack.append(s[i])
            if s[i] in [')','}',']']:
                if stack== []:
                    return False
                if mappy[s[i]]!=stack[-1]:
                    return False
                if mappy[s[i]]==stack[-1]:
                    stack.pop(-1)  
                 
        return True if stack==[] else False       
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mappy= {')':'(', '}':'{', ']':'['}
        if len(s)==1:
            return False
        for i in range(len(s)):
            if s[i]in {"(", "{", "["}:
                stack.append(s[i])
            elif s[i] in {")", "}", "]"}:
                if stack==[]:
                    return False
                if mappy[s[i]]!=stack[-1]:
                    return False
                else:
                    stack.pop()
        return not stack        
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid < x:
                left = mid + 1
            elif mid * mid > x:
                right = mid -1
            else:
                return mid
        return right

