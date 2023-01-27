'''
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        if len(nums) == 3:
            return sum(nums)
        

        temp = sorted(nums)

        out = temp[0] + temp[1] +temp[2]
        #dist = temp[0] + temp[1] +temp[2]

        for i in range(len(temp) -2):
            if i > 0 and temp[i] == temp[i-1]:
                continue

            r = len(temp) -1
            l = i +1

            while l < r and i < l:
                s = temp[i] + temp[l] +temp[r]
                
                if s == target:
                    return s
                
                if abs(s-target) < abs(out-target):
                    out = s
                
                if s < target:
                    l += 1
                else:
                    r -= 1
        
        return out