def getIdenticalTwinsCount(self, arr: List[int]) -> int:
    left=0
    right=1
    twin=0
    while left<len(arr):
        if right>len(arr)-1:
            left=left+1
            right=left+1
        elif arr[left]==arr[right]:
            twin+=1
            right+=1
        else:
            right+=1
    return twin