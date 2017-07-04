/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

//1. recursive solution
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {       
        vector<int>* rt = new vector<int>();
		traversal(root, *rt);
        return *rt;
    }
    
    void traversal(TreeNode* root, vector<int>& v) {
        if (root == NULL) {
            return;
        }
        if (root->left != NULL) {
            traversal(root->left, v);
        } 
        v.push_back(root->val);
        
        if (root->right != NULL) {
            traversal(root->right, v);
        }
    }
};

//2. iterative solution
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int>* rt = new vector<int>();
        if (root == NULL) return *rt;
        
        vector<TreeNode *>* stack = new vector<TreeNode*>();
        TreeNode* cur = root;
                
        while (cur != NULL || stack->size() > 0) {
            if (cur != NULL) {
                stack->push_back(cur);
                cur = cur->left;
            } else {
                TreeNode* tmp = stack->back();
                stack->pop_back();
                rt->push_back(tmp->val);
                cur = tmp->right;
            }
            
        }
        return *rt;
    }
};