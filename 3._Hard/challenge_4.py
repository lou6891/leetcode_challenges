'''

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        temp = sorted(nums1 + nums2)

        if len(temp) % 2 != 0:
            a =int((len(temp) -1) / 2 )
            return temp[a]

        else :
            a = int((len(temp)/2 )-1)
            b = int(len(temp) / 2)
            return (temp[a] + temp[b]) / 2