"""
650. 2 Keys Keyboard
Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.

Example 1:
Input: 3
Output: 3
Explanation:
Intitally, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.
Note:
The n will be in the range [1, 1000].
"""
#����������n�������ҵ�����paste������ ����18���Էֽ�Ϊ 9*2�� 9�ֿ��Էֽ�Ϊ3*3. ������̾���
#�ҵ�n���Ա���Щ���������Ĺ���.

class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(2, n + 1):
            while n % i == 0:
                count += i
                n = n //i
        return count
        

#�ݹ鷽��
class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rty
        """
        if n == 1: return 0
        for i in range(2, n+1):
            if n % i != 0:
                 continue
            else:
                return (i + self.minSteps(n // i) )     
        