#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
# https://leetcode.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (45.90%)
# Likes:    3485
# Dislikes: 82
# Total Accepted:    581.4K
# Total Submissions: 1.3M
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric
# around its center).
# 
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
# 
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 
# 
# But the following [1,2,2,null,3,null,3] is not:
# 
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 
# 
# Follow up: Solve it both recursively and iteratively.
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
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        boool=True

        n1=root
        n2=root
        def compare(n1,n2):
            if n1 is None and n2 is None:
                return True

            if n1 is None and n2 is not None:
                return False
            if n1 is not None and n2 is None:
                return False

            if n1.val != n2.val:
                return False

            
            if not compare(n1.left,n2.right):
                return False
            if not compare(n1.right,n2.left):
                return False
            return True

        return (compare(n1,n2))
        
# @lc code=end

