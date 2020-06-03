#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (52.75%)
# Likes:    2481
# Dislikes: 64
# Total Accepted:    545.8K
# Total Submissions: 1M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
# 
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 
# return its level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return None
        q=[]
        globals=[]
        level=1
        q.append([root.val])
        def traversal(root,level):
            globals.append(level)
            
            q.append([])
            
            if root is None:
                return 
            if root.left:
                q[level].append(root.left.val)
            if root.right:q[level].append(root.right.val)
            traversal(root.left,level+1)
            traversal(root.right,level+1)

        
        traversal(root,level)
        print(globals)
        newq=q[0:max(globals)-1]
        return newq

        
# @lc code=end

