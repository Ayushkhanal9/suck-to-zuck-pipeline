def getCumulativeSum(self, arr: List[int]) -> List[int]:
    # add your logic here
    for i in range(len(arr)):
        if i !=0:
            arr[i]=arr[i]+arr[i-1]
    return arr