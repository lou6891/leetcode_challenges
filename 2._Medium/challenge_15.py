'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        n = len(nums)
        nums.sort()
        
        out = []
        o = []


        for a in range(n - 2):

            if a>0 and nums[a] == nums[a-1]:
                continue

            l = a + 1
            r = n -1

            while l < r:

                if nums[a] + nums[l] + nums[r] > 0:
                    r -= 1

                elif nums[a] + nums[l] + nums[r] < 0:
                    l += 1

                else:
                    out.append([nums[a], nums[l] , nums[r] ])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return out

            

    