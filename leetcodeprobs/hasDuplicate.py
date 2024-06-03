#program to see if an array has a du[plicate
def containsDuplicate(self, nums: List[int]) -> bool:
    mappy={}
    for i in range(len(nums)):
        if nums[i] not in mappy:
            mappy[nums[i]]=1
        elif nums[i] in mappy:
            return True
    return False