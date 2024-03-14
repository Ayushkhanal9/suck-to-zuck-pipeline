# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists 
#intersect. If the two linked lists have no intersection at all, return null.
# For example, the following two linked lists begin to intersect at node c1:
# The test cases are generated such that there are no cycles anywhere in the entire linked structure.
# Note that the linked lists must retain their original structure after the function returns.
# Custom Judge:
# Example 1:
# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
# Output: Intersected at '8'
# Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
# From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 
#nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
# - Note that the intersected node's value is not 1 because the nodes with value 1 in A and B (2nd node in A and 
#3rd node in B) are different node references. In other words, they point to two different locations in memory, 
#while the nodes with value 8 in A and B (3rd node in A and 4th node in B) point to the same location in memory.

# first solution without using set() and using length to solve the problem
def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    curr1=headA
    curr2=headB
    length1=0
    length2=0

    while curr1:
        length1+=1
        curr1=curr1.next
    curr1=headA

    while curr2:
        length2+=1
        curr2=curr2.next
    curr2=headB

    if length1 <length2:
        diff=length2-length1
        for i in range(0,diff):
            curr2=curr2.next
    elif length2 <length1:
        diff=length1-length2
        for i in range(0,diff):
            curr1=curr1.next

    while curr1 and curr2:
        
        if  curr1==curr2:
            return curr1
            
        curr1=curr1.next
        curr2=curr2.next
    return None

#2nd solution using set()
def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    curr1=headA
    curr2=headB
    map=set()
    while curr1:
        map.add(curr1)
        curr1=curr1.next
    while curr2:
        if curr2 in map:
            return curr2
        curr2=curr2.next
    return None

#using just an array
def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    curr1=headA
    curr2=headB
    map=[]
    while curr1:
        map.append(curr1)
        curr1=curr1.next
    while curr2:
        if curr2 in map:
            return curr2
        curr2=curr2.next
    return None