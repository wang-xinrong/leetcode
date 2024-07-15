# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev=ListNode(next=head)
        l=0
        hashmap=[]
        while prev.next:
            hashmap.append(prev.next)
            prev=prev.next
            l+=1
        if n < l:
            hashmap[-n-1].next=hashmap[-n].next
        else:
            head=head.next
        return head
    def removeNthFromEndTwoPointer(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast=slow=head

        for _ in range(n):
            fast=fast.next
        if not fast:
            return head.next

        while fast.next:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return head
