class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        for i in range(len(nums) +1):
            if sum(nums[:i]) == sum(nums[i +1:]) and i != len(nums):
                return i
        else:
            return -1