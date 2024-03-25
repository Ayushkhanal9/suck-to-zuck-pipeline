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