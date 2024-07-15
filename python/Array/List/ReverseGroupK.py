# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr=dummy=ListNode(next=head)
        while curr.next:
            prev=curr
            curr=curr.next
            test=prev
            count=0
            while test.next and count<k:
                test=test.next
                count+=1
            if count!=k:
                break
            i=0
            while curr.next and i < k-1:
                nextnode = curr.next
                prev.next, curr.next, nextnode.next=nextnode, nextnode.next, prev.next
                i+=1
        return dummy.next

            