# 问题：输出二叉树每一层的最大值
# 思路：广度优先搜索，每一层之间用#分隔，求最大值

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        res = []
        queue = [root, "#"]
        maxnum = root.val
        while queue:
            root = queue.pop(0)
            if root == "#":
                if queue: queue.append("#")
                res.append(maxnum)
                maxnum = float("-inf")
                continue
            maxnum = max(maxnum, root.val)
            if root.left: queue.append(root.left)
            if root.right: queue.append(root.right)
        return res

#方案二： 深度优先， 每次递归记录层数
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(node, h):
            if not node: return
            if h >= len(res):
                res.append(node.val)
            else:
                res[h] = max(res[h], node.val)
            dfs(node.left, h+1)
            dfs(node.right, h+1)
            
        res = []
        dfs(root, 0)
        return res
        

    