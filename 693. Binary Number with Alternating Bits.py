class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        v = str(bin(n))
        l = list(v)
        for i in range(2, len(v)):
            if (i + 1) >= len(v):
                return True
            if l[i] == l[i+1]:
                return False
        
        return True



# bit operation method

class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        last = n & 1
        while (n // 2 > 0):
            n = n //2
            c = n & 1
            if (c == last):
                return False
            last = c
        return True