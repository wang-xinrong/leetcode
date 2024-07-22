"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cache={}
        def helper(node:Optional['Node']):
            if not node:
                return None
            if node.val not in cache:
                newnode=Node(node.val, [])
                cache[node.val]=newnode
                for n in node.neighbors:
                    newnode.neighbors.append(helper(n))
            return cache[node.val]

        helper(node)
        return cache[node.val] if node else None
    
    def cloneGraphReplacingCallStackWithDeque(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        d=deque([node])
        dic={node.val: Node(node.val, [])}
        while d:
            curr=d.popleft()
            currclone=dic[curr.val]
            for n in curr.neighbors:
                if n.val not in dic:
                    dic[n.val]=Node(n.val, [])
                    d.append(n)
                currclone.neighbors.append(dic[n.val])
        return dic[node.val]