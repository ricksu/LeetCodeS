#��������

#window���ڴ��'��ʱ'����Ҫ��ľ���С��k��item�� 
#����鵽 r-l =k ������Ҫ��ʱ�� ɾ��window�е����item

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
        