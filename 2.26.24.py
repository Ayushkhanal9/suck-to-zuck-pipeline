from typing import Optional

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
def linked_list_to_list(node):
    elements = []
    while node:
        elements.append(node.val)
        node = node.next
    return elements

# Test cases
test_cases = [
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], 5),
    ([], [], -1),
    ([1], [1], 1),
    ([1, 2], [2, 1], 2)
]

for input_list, expected_output, max_val in test_cases:
    input_linked_list = list_to_linked_list(input_list)
    found_max, reversed_linked_list = reverseList(input_linked_list)
    output_list = linked_list_to_list(reversed_linked_list)
    assert output_list == expected_output, f"Test case {input_list} failed, expected {expected_output}, got {output_list}"
    assert found_max == max_val
print("All test cases passed!")
