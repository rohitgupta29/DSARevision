
"""Concepts"""
from http.cookiejar import vals_sorted_by_key

"""reverse a linked list"""


"""Remove nth node from the end of list"""

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head,n):

    dummy = ListNode(0)
    dummy.next = head

    first = dummy
    second = dummy

    for _ in range(n+1):
        first = first.next

    while first:
        first = first.next
        second = second.next

    second.next = second.next.next

    return dummy.next

"""Middle of a linked list"""


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def middleNode(head):

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# Example usage:
# Create the linked list 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

result = middleNode(head)

# Function to print the linked list from a given node
def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Print the result
print_linked_list(result)  # Output: 3 -> 4 -> 5 -> None



"""Delete node in a linked list"""


class ListNode:
    def __init__(self,val, next = None):
        self.val = val
        self.next = next

def deleteNode(node):

    node.val = node.next.val
    node.next = node.next.next


"""merge two sorted lists"""

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):

    dummy = ListNode(0)
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next  = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    if l1:
        current.next = l1
    elif l2:
        current.next = l2

    return dummy.next


"""Linked list cycle"""


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def hasCycle(head):

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False

