"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        cache=dict()
        def traverse(root: 'Node', depth: int):
            if not root:
                return
            
            if root.left:
                if depth not in cache:
                    cache[depth]=[root.left]
                else:
                    cache[depth].append(root.left)
                traverse(root.left, depth+1)

            if root.right:
                if depth not in cache:
                    cache[depth]=[root.right]
                else:
                    cache[depth].append(root.right)
                traverse(root.right, depth+1)

        traverse(root, 0)
        for list in cache.values():
            i = 0
            while i < len(list) - 1:
                list[i].next = list[i+1]
                i+=1
        return root
    
    def connectFaster(self, root: 'Node') -> 'Node':
        self.rootnode=root
        child=temp=Node(0)
        while root:
            while root:
                if root.left:
                    child.next=root.left
                    child=child.next
                if root.right:
                    child.next=root.right
                    child=child.next
                root=root.next
            root = temp.next
            child = temp
            child.next = None
        return self.rootnode
        