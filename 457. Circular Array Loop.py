"""
You are given an array of positive and negative integers. If a number n at an index is positive, then move forward n steps. Conversely, if it's negative (-n), move backward n steps. Assume the first element of the array is forward next to the last element, and the last element is backward next to the first element. Determine if there is a loop in this array. A loop starts and ends at a particular index with more than 1 element along the loop. The loop must be "forward" or "backward'.

Example 1: Given the array [2, -1, 1, 2, 2], there is a loop, from index 0 -> 2 -> 3 -> 0.

Example 2: Given the array [-1, 2], there is no loop.

Note: The given array is guaranteed to contain no element "0".

Can you do it in O(n) time complexity and O(1) space complexity?
"""

class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def getNext(pos, nums, dir):
            if dir * nums[pos] < 0: return -1
            x = pos + nums[pos]
            if (x >= len(nums)): x -= len(nums)
            elif (x < 0): x += len(nums)
            if (x == pos): return -1  
            return x
        
        def getNextTwo(pos, nums, dir):
            x = getNext(pos, nums, dir)
            if (x == -1 or dir * nums[pos] < 0): return -1
            return getNext(x, nums, dir)
        
        for i in range(0, len(nums)) :
            if (nums[i] == 0): continue
            slow, fast = i, i
            if (nums[i] > 0): dir = 1
            else: dir = -1                
            while(getNext(slow, nums, dir) != -1 and getNextTwo(fast, nums, dir) != -1):
                slow = getNext(slow, nums, dir)
                fast = getNextTwo(fast, nums, dir)
                if (fast == slow): return True
            
            slow = i
            while(getNext(slow, nums, dir) != -1):
                nums[slow] = 0
                slow = getNext(slow, nums, dir)
                
        return False