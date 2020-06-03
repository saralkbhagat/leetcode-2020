#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (42.76%)
# Likes:    1898
# Dislikes: 150
# Total Accepted:    414.4K
# Total Submissions: 969.1K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, determine if it is height-balanced.
# 
# For this problem, a height-balanced binary tree is defined as:
# 
# 
# a binary tree in which the left and right subtrees of every node differ in
# height by no more than 1.
# 
# 
# 
# 
# Example 1:
# 
# Given the following tree [3,9,20,null,null,15,7]:
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# Return true.
# 
# Example 2:
# 
# Given the following tree [1,2,2,3,3,null,null,4,4]:
# 
# 
# ⁠      1
# ⁠     / \
# ⁠    2   2
# ⁠   / \
# ⁠  3   3
# ⁠ / \
# ⁠4   4
# 
# 
# Return false.
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
    def isBalanced(self, root: TreeNode) -> bool:
        flag=[True]
        if root is None:
            return True

        def height(root):
            if root is None:
                return 0
            left=height(root.left)
            right=height(root.right)
            h=max(left,right)+1
            return h
        def bal(root):
            if root is None:
                return
            Lheight=height(root.left)
            Rheight=height(root.right)
            absheight=Lheight-Rheight
            if abs(absheight)>1:
                flag.append(False)
            bal(root.left)

            bal(root.right)

            return 
        bal(root)
        return flag[-1]
        
# @lc code=end

