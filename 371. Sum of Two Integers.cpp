/*
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.
*/

class Solution {
public:
    int getSum(int a, int b) {
        while (b != 0) {
            int aa = a^b;//不进位的加法
            int bb = (a & b) << 1;//各个位上的进位值
            a = aa;
            b = bb;
        }
        return a;
    }
};