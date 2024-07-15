from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        stack=[]
        i = 0
        left-=1
        right-=1
        curr = head
        leftend = None
        rightend = None
        while curr:
            if i == left-1:
                leftend = curr
            elif i == right + 1:
                rightend = curr
            elif i >= left and i <= right:
                stack.append(curr)
            curr = curr.next
            i+=1
        if stack:
            stack[0].next = None
            
        for i in range(len(stack)-1, 0, -1):
            stack[i].next = stack[i-1]
        if leftend and stack:
            leftend.next = stack[-1]
        if rightend and stack:
            stack[0].next = rightend
        if not leftend:
            head = stack[-1]
        return head
    
    def reverseBetweenTwoPointer(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left==right:
            return head
        prev = dummy = ListNode(next=head)

        for _ in range(left-1):
            prev = prev.next

        curr=prev.next
        
        for _ in range(right-left):
            nextnode = curr.next
            prev.next, curr.next, nextnode.next = nextnode, nextnode.next, prev.next
        return dummy.next


        