from typing import Optional,List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# [max_val_of_linked_list, head of reversed linked list]
        
def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev=None
    curr= head
    max_val=0
    print(curr)
    if curr == None:
        return [-1,[]]
    while curr!= None:
        if max_val< curr.val:
            max_val=curr.val

        next=curr.next
        curr.next= prev
        prev= curr

        curr= next

    return [max_val,prev]





# Helper function to convert a list to a linked list
def list_to_linked_list(elements):
    head = None
    for element in reversed(elements):
        head = ListNode(element, head)
    return head

# Helper function to convert a linked list to a list
# def linked_list_to_list(node):
#     elements = []
#     while node:
#         elements.append(node.val)
#         node = node.next
#     return elements

# # Test cases
# test_cases = [
#     ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], 5),
#     ([], [], -1),
#     ([1], [1], 1),
#     ([1, 2], [2, 1], 2)
# ]

# for input_list, expected_output, max_val in test_cases:
#     input_linked_list = list_to_linked_list(input_list)
#     found_max, reversed_linked_list = reverseList(input_linked_list)
#     output_list = linked_list_to_list(reversed_linked_list)
#     assert output_list == expected_output, f"Test case {input_list} failed, expected {expected_output}, got {output_list}"
#     assert found_max == max_val
# print("All test cases passed!")


#prices and prices[i] returns the price of the stock on the ith day
#sliding window max price, every i is a day
def maxProfit(prices: List[int]) -> int:
        profit=0
        j=1
        i =0
        index=0
        while i<j and j < len(prices):
            print(prices[i],prices[j],index,profit)
            if j>=len(prices) and profit==0:
                return index
            if prices[j]<prices[i]:
                i=i+1
                j=i+1
            elif prices[j]-prices[i]>profit:
                profit=prices[j]-prices[i]
                index=j
                j=j+1
            else:
                j=j+1
        return profit
                
        
                

def test_max_profit():
    # Test 6: Large list with multiple fluctuations
    assert maxProfit([10, 22, 5, 75, 65, 80]) == 75, "Test 6 Failed"

    # Test 1: Prices fluctuate with profit
    assert maxProfit([7, 1, 5, 3, 6, 4]) == 5, "Test 1 Failed"

    # Test 2: Prices are in descending order, no profit
    assert maxProfit([7, 6, 4, 3, 1]) == 0, "Test 2 Failed"

    # Test 3: Prices are in ascending order, maximum profit
    assert maxProfit([1, 2, 3, 4, 5]) == 4, "Test 3 Failed"

    # Test 4: Only one price, no profit
    assert maxProfit([5]) == 0, "Test 4 Failed"

    # Test 5: Prices are the same, no profit
    assert maxProfit([3, 3, 3, 3, 3]) == 0, "Test 5 Failed"

    # Test 7: Profit at the beginning
    assert maxProfit([10, 20, 10, 20, 10]) == 10, "Test 7 Failed"

    # Test 8: Random fluctuating prices
    assert maxProfit([3, 8, 2, 10, 4, 1, 7]) == 8, "Test 8 Failed"

test_max_profit()
print("All tests passed!")

