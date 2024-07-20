class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.list=[]
        self.pointer=0
        self.inorderTraversal(root)

    def next(self) -> int:
        val=self.list[self.pointer]
        self.pointer+=1
        return val

    def hasNext(self) -> bool:
        return self.pointer<len(self.list)

    def inorderTraversal(self, root: Optional[TreeNode]):
        if not root:
            return
        self.inorderTraversal(root.left)
        self.list.append(root.val)
        self.inorderTraversal(root.right)

class BSTIteratorFaster:
    def __init__(self, root: Optional[TreeNode]):
        self.stack=[]
        self.pushall(root)

    def next(self) -> int:
        temp=self.stack.pop()
        self.pushall(temp.right)
        return temp.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def pushall(self, root: Optional[TreeNode]):
        while root:
            self.stack.append(root)
            root=root.left