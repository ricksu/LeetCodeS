class Solution(object):
	def merge(self, nums1, m, nums2, n):
	    """
	    :type nums1: List[int]
	    :type m: int
	    :type nums2: List[int]
	    :type n: int
	    :rtype: void Do not return anything, modify nums1 in-place instead.
	    """

	    m, n, t = m -1, n - 1, m + n - 1
	    while m >= 0 and n >= 0:
	    	if nums1[m] > nums2[n]:
	    		nums1[t] = nums1[m]
	    		m -= 1
	    	else:
	    		nums1[t] = nums2[n]
	    		n -= 1
	    	t -= 1
	    if n >= 0:
	    	nums1[:n+1] = nums2[:n+1]

def test():
	n1=[1, 2, 5, 10]
	n2=[5, 8, 100, 200, 1000, 2000]
	n1_len= len(n1)
	n1 = n1 + [0]*len(n2)
	
	merge = Solution()
	merge.merge(n1, n1_len, n2, len(n2))
	print n1

test()


