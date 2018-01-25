"""
Given an array of integers, return indices of the two numbers such that they add up to a specific
target.

You may assume that each input would have exactly one solution, and you may not use the same element
twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = sorted([num, i] for i, num in enumerate(nums))
        l, r = 0, len(nums) -1
        while l < r:
            sums = nums[l][0] + nums[r][0]
            if sums == target:
                return [nums[l][1], nums[r][1]]
            elif sums < target:
                l += 1
            else:
                r -= 1
        
        return
                
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = 0
        total = len(nums)
        res = []
        
        d = {}
        for i, n in enumerate(nums):
            if target - n in d:
                return [i, d[target -n]]
            d[n] = i

        return 
