class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        a = ""
        for i in digits:
            a = a + str(i)
        
        a = int(a) + 1
        a = str(a)
        
        b = [int(x) for x in a]
        return b
        