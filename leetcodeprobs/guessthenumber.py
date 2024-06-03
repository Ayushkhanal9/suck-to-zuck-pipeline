# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
#in binary search we have to move the high and low by +1 or -1 cause thats the only way it will see movement
class Solution:
    def guessNumber(self, n: int) -> int:
        low=1
        mid=0

        while low<=n:
            mid=(low+(n-low)//2)
            result=guess(mid)
            if result== 1:
                low=mid+1
            elif result== -1:
                n=mid-1
            else:
                return mid
        return mid