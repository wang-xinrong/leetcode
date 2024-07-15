from typing import Optional

"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr = head
        dict={}
        while curr:
            dict[curr] = Node(curr.val)
            curr=curr.next
        curr=head
        while curr:
            dict[curr].next = dict.get(curr.next)
            dict[curr].random = dict.get(curr.random)
            curr=curr.next
        return dict[head]