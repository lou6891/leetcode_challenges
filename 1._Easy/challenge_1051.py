class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        exp = list(x for x in heights)
        exp.sort()
        counter = 0
        for i,v in enumerate(heights):
            if v != exp[i]:
                counter += 1
        
        return counter