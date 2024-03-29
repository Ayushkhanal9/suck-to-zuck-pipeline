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

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        elif list1 is None and list2 is not None:
            return list2
        elif list1 is not None and list2 is None:
            return list1
        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        curr = head
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2

        return head
    
    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        temp=root.left
        root.left=root.right
        root.right=temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        array=[]
        curr=head
        while curr is not None:
            if curr not in array:
                array.append(head)
                curr=curr.next
            print(array)
            if curr in array:
                return True
        return False