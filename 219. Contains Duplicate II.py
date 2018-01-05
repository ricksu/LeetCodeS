#滑动窗口

#window用于存放'暂时'符合要求的距离小于k的item， 
#当检查到 r-l =k 不符合要求时， 删除window中的这个item

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums or k == 0:
            return False
        
        window, l = set(), 0
        for r, num in enumerate(nums):
            if num in window:
                return True
            if r - l == k:
                window.remove(nums[l])
                l += 1
            window.add(num)
        return False
        