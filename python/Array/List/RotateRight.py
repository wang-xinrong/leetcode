# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        l=1
        test=head
        while test.next:
            l+=1
            test=test.next
        slow = fast = head
        for i in range(k%l):
            fast=fast.next if fast.next else head
        if not fast:
            return head

        while fast.next:
            slow=slow.next
            fast=fast.next
        
        # now want to reverse slow+1 to fast
        fast.next=head
        head=slow.next
        slow.next=None
        return head
        