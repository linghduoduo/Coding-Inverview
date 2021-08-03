class treeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def hasSubtree(self, root1, root2):
        if not root1 or not root2:
            return False

        return self.isSubtree(root1, root2) or self.hasSubtree(root1.left, root2) or self.hasSubtree(root1.right, root2)

    def isSubtree(self, root1, root2):
        if root2:
            return True
        if not root1:
            return False
        if root1.val != root2.val:
            return False
        return isSubtree(root1.left, root2.left) and isSubtree(root1.right, root2.right)

if __name__ == '__main__':
    root1 = treeNode(8)
    root1.left = treeNode(8)
    root1.left.left = treeNode(9)
    root1.left.right = treeNode(2)   
    root1.right = treeNode(7)
    root1.right.left = treeNode(1)
    root1.right.right = treeNode(1) 

    root2= treeNode(8)
    root2.left = treeNode(9)
    root2.right = treeNode(2)     

    res = Solution().hasSubtree(root1, root2)
    print(res)
