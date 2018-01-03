#对每个房子进行查找， 找到最小距离。这些距离中的最大值， 就是最小半径.

class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        #二分查找， 查找比house大的最小heater index
        def bineary_search(heaters, house):
            if house > heaters[-1]:return -1
            l, r = 0, len(heaters) - 1
            while l < r:
                m = l + (r -l)/2
                if heaters[m] > house:
                    r = m
                else:
                    l = m + 1
            return l
        
        houses.sort()
        heaters.sort()
        res = 0
        for house in houses:
            index = bineary_search(heaters, house)
            #查找heater位置， 可能在结尾、开头或者中间
            if index == -1:
                res = max(res, house - heaters[-1])
            elif index == 0:
                res = max(res, heaters[0] - house)
            else :
                res = max(res, min(house - heaters[index - 1], heaters[index] - house))
        return res
        