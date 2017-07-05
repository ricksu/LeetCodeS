/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> findFrequentTreeSum(TreeNode* root) {
        vector<int> results;
        if (root == NULL) return results;
        
        std::map <int, int> mpa;// map to store the sum values and count
        nodeSum(root, mpa);
        
        //sort the map by count
        vector<pair<int, int>> temp;
        for(auto a:mpa) temp.push_back({a.second, a.first});
        sort(temp.begin(), temp.end());
        
        //put the last item value
        results.push_back(temp.back().second);
        int i = temp.size() - 1;
        //put other values if any
        while(i - 1 >= 0 && temp[i].first == temp[i - 1].first) {
            i--;
            results.push_back(temp[i].second);
        }
        return results;
    }
    
    int nodeSum(TreeNode* node, std::map <int, int>& mp) {
        if (node == NULL) return 0;
        int sum = node->val;
        if (node->left != NULL) {
            sum += nodeSum(node->left, mp);
        }
        if (node->right != NULL) {
            sum += nodeSum(node->right, mp);
        }
        // if(mp.find(sum) == mp.end()) {
        //     mp[sum] = 1;
        // } else {
        //     mp[sum] += mp[sum];
        // }
        mp[sum]++;
        cout << "sum="<< sum<<endl;
        return sum;
    }
};