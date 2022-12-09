class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr_len = len(nums)/2

        s = set(nums)

        for x in s:
            if nums.count(x) > arr_len:
                return x