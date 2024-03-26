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
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums*2


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans=[]
        ans.append(-1)
        biggest=0
        if len(arr)==1:
            return [-1]
        for i in range(len(arr)-1,-1,-1):
            if i==0:
                return reversed(ans)
            biggest=max(biggest,arr[i])
            if i==len(arr)-1:
                ans.append(biggest)
            elif biggest>arr[i-1]:
                ans.append(biggest)
            else:
                ans.append(biggest)
        return -1
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left=right=0
        strs=''
        if s is None:
            return True
        for right in range(len(t)):
             if left>=len(s):
                return True if strs==s else False
             if s[left]==t[right]:
                 left+=1
                 strs+=t[right]
        return True if strs==s else Fals
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        value = 0
        counter = 0
        print(len(s))
        for i in range(len(s)):
            if s[i]==" ":
                if counter >=1:
                    value=counter
                counter =0
            else:
                counter+=1
        return counter if counter>0 else value