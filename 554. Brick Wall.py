#��ÿ��ש��edge�����ֵ䣬ÿһ�ж��ֵ��е�edge���м��Ϳ�����, ����+1.

class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        d = collections.defaultdict(int)
        for w in wall:
            cumsum = 0
            for block in w:
                cumsum += block
                d[cumsum] += 1
        
        #��Եֵ��Ϊ0
        d[sum(wall[0])] = 0

        return len(wall) - max(d.values())



## ������ⷨ�� ��ʱ:(
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        edges=[]
        for i in range(0, len(wall)):
            edge = set()
            cur = 0
            for j in range(0, len(wall[i])):
                cur += wall[i][j]
                if (j != (len(wall[i]) - 1)):
                    edge.add(cur)
               
            edges.append(edge)
        #for k in range(0, len(edges)):
        #    print edges[k]
            
        s = set()
        for e in edges:
            for m in e:
                s.add(m)
        #print "final", s
        if (len(s) == 0): return len(wall)
        
        cross = sys.maxint
        for i in s:
            cur =0
            for k in edges:
                if i in k:
                    continue
                else:
                    cur += 1                    
                    #print i, " cross:" , k
            #print "pass ", i, "cross=",cross, "cur=",cur
            if cross > cur:
                cross = cur
        
        #print "======", cross
        return cross
        