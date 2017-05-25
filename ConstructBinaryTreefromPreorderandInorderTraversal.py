#!/usr/bin/env python
# -*- coding:utf-8 -*-   
# Author:zouzhipeng
"""
LeetCode 105
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0 or len(preorder) != len(inorder):
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        for i, key in enumerate(inorder):
            if key == preorder[0]:
                index = i
                break
        left = self.buildTree(preorder[1:index+1], inorder[:index])
        right = self.buildTree(preorder[index+1:], inorder[index+1:])
        root.left = left
        root.right = right
        return root

"""
leetcode 106
Construct Binary Tree from Inorder and Postorder Traversal
中序遍历和后续遍历，求二叉树
"""


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(postorder) > 0:
            index = inorder.index(postorder[-1])
            root = TreeNode(inorder[index])
            root.left = self.buildTree(inorder[:index], postorder[:index])
            root.right = self.buildTree(inorder[index+1:], postorder[index:-1])
            return root
        return None

