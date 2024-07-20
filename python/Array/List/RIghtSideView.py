# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # condition for the node to be included:
        # if we keep travelling down right path, the first appearing on each depth
        # O(n) is necessary as we need to traverse the whole tree

        def traverseRight(root: Optional[TreeNode], depth: int):
            if not root:
                return
            if depth>len(view):
                view.append(root.val)

            traverseRight(root.right, depth+1)
            traverseRight(root.left, depth+1)

        view=[]
        traverseRight(root, 1)
        return view

        