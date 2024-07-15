from typing import Optional 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        overflow=0
        sum=0
        res=[]
        curr_up = l1
        curr_lo = l2
        while (curr_up is not None) and (curr_lo is not None):
            sum=curr_up.val + curr_lo.val + overflow
            overflow=sum//10
            sum=sum%10
            curr_lo.val = sum
            curr_up=curr_up.next
            if curr_lo.next is None:
                last_curr_lo = curr_lo
                bridged_gap = False
            curr_lo=curr_lo.next
        if curr_up is not None:
            while (curr_up is not None):
                sum=curr_up.val + overflow
                overflow=sum//10
                sum=sum%10
                if not bridged_gap:
                    bridged_gap=True
                    curr_lo=last_curr_lo
                curr_lo.next = ListNode(sum, None)
                curr_lo=curr_lo.next
                curr_up=curr_up.next
                if curr_up is None:
                    last_curr_lo = curr_lo
        elif curr_lo is not None:
            while (curr_lo is not None):
                sum=curr_lo.val + overflow
                overflow=sum//10
                sum=sum%10
                curr_lo.val = sum
                if curr_lo.next is None:
                    last_curr_lo = curr_lo
                curr_lo=curr_lo.next

        if overflow > 0:
            last_curr_lo.next = ListNode(overflow, None)
        return l2
    
    def addTwoNumbersNewNodes(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = dummyHead.next
        dummyHead.next = None
        return result