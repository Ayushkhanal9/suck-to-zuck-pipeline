def sortedSquares(self, nums: List[int]) -> List[int]:
    squared=[]
    for i in range(len(nums)):
        square=nums[i]**2
        squared.append(square)
    squared.sort()    
    return squared