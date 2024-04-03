class Solution:
    def repeatedCharacter(self, s: str) -> str:
        for i in range(len(s)):
            c = s[i]
            for j in range(i):
                if s[j] == c:
                    return c
        return ""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mappy = {}
        for i in range(len(nums)):
            num = nums[i]
            compl = target - num
            if compl in mappy:
                return [i, mappy[compl]]
            mappy[num] = i
        
        return [-1, -1]
class Solution:
    def arrangeCoins(self, n: int) -> int:
        counter=n
        steps =0
        for i in range(1,n+1):
            if counter-i<0:
                return steps-1
            counter = n - i
            steps+=1 
        return steps
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
