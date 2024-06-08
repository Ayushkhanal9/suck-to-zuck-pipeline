def getCumulativeSum(self, arr: List[int]) -> List[int]:
    # add your logic here
    for i in range(len(arr)):
        if i !=0:
            arr[i]=arr[i]+arr[i-1]
    return arr
def getPositiveCumulativeSum(self, arr: List[int]) -> List[int]:
    n=len(arr)
    posCum=[]
    if arr[0]>0:
        posCum.append(arr[0])
    for i in range(1,n):
        if i !=0:
            arr[i]=arr[i-1]+arr[i]
            if arr[i]>0:
                posCum.append(arr[i])
    return posCum