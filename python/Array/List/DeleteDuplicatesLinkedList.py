# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=dummy=ListNode(next=head)
        curr=prev.next
        while curr and curr.next:
            while curr.next and curr.val == curr.next.val:
                curr=curr.next
            if prev.next != curr:
                prev.next=curr.next
            else:
                prev=curr
            curr=curr.next
        return dummy.next