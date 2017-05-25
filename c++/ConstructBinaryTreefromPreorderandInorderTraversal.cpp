#include <iostream>
#include <vctor>
using namespace std;
using std::vector;

//Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};


class Solution {
public:
    TreeNode* buildRoot(vector<int>& preorder, vector<int>& inorder, int i , int j, int k, int l) {
        if(j<i) return nullptr;
        TreeNode* node = new TreeNode(preorder[i]);
        int pos;
        for(int t = k;t<=l;t++) {
            if(inorder[t] == preorder[i]) {
                pos = t;
                break;
            }
        }
        node->left = buildRoot(preorder, inorder, i+1, i+pos-k, k, pos-1);
        node->right = buildRoot(preorder, inorder, j-k+pos+1, j,pos+1, l);
        return node;
    }

    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return buildRoot(preorder, inorder, 0, preorder.size()-1, 0, inorder.size()-1);
    }
};


// 已知中序和后序，求二叉树
class Solution {
public:
    TreeNode* help(vector<int>& inorder, vector<int>& postorder, int is, int ie, int ps, int pe) {
        if(is > ie) return nullptr;
        TreeNode* node = new TreeNode(postorder[pe]);
        int pos;
        for(int i = is;i<=ie;i++) {
            if(inorder[i] == postorder[pe]) {
                pos = i;
                break;
            }
        }
        node->left = help(inorder, postorder, is, pos-1, ps, ps+pos-is-1);
        node->right = help(inorder, postorder, pos+1, ie, ps+pos-is, pe-1);
        return node;
    }

    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        return help(inorder, postorder, 0, inorder.size()-1, 0, postorder.size()-1);
    }
};

// 1 2 3 4 5
// 4 3 5 2 1