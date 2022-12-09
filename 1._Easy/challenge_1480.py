class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        for i in range(1, len(nums) +1):
            ret.append(sum(nums[:i]))  

        return ret