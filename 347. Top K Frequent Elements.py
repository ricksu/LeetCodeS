"""
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 ¡Ü k ¡Ü number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dt = collections.defaultdict(int)
        for i in nums:
            dt[i] += 1
        i = 0
        rt=[]
        for key, value in sorted(dt.iteritems(), key=lambda (k,v): (v,k), reverse=True):
            if (i < k):
                rt.append(key)
                i += 1

        return rt
        