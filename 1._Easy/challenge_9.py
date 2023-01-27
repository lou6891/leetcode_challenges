'''
Given an integer x, return true if x is a 
palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
'''
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        x = [x for x in str(x)]

        b = [x[i] for i in range(len(x)-1, -1, -1)]

        if x == b:
            return True
        else:
            return False


