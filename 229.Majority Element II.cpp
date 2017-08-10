/*
Given an integer array of size n, find all elements that appear more than ? n/3 ? times.
The algorithm should run in linear time and in O(1) space.
*/

//Boyer-Moore Algorithm. Reference at https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html
class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        vector<int> answer;
        int n1, n2, r1, r2;
        n1 =  n2 = r1 = r2 = 0;
        for (int num: nums) {
            if (num == n1) {
                r1++;
            } else if (num == n2) {
                r2++;
            } else if (r1 == 0) {
                r1++;
                n1 = num;
            } else if (r2 == 0) {
                r2++;
                n2 = num;
            } else {
                r1--;
                r2--;
            }
        }
        
        r1 = 0;
        r2 = 0;
        for (int num: nums) {
            if (num == n1) r1++;
            else if (num == n2) r2++;
        }
        int n = (int) nums.size();
        if (r1 > n / 3) answer.push_back(n1);
        if (r2 > n / 3) answer.push_back(n2);
        return answer;
    }
};