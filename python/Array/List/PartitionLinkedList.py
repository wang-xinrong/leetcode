# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = right = head
        while left and left.val >= x:
            left = left.next
        leftstart = left
        while right and right.val < x:
            right = right.next
        if not left or not right:
            return head
        rightstart = right
        while head:
            if head != left and head.val < x:
                left.next = head
                left = left.next
            elif head != right and head.val >= x:
                right.next = head
                right = right.next
            head = head.next
        right.next = None
        left.next = rightstart
        return leftstart