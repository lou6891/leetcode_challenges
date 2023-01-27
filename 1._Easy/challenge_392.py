'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
'''

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = list(s)
        t = list(t)


        tester = []

        if len(s) > len(t):
            return False

        elif len(s) == 0:
            return True

        else:
            counter = 0
            for i in t:
                for j in range(counter, counter +1 ):
                    if s[j] == i:
                        tester.append(s[j])
                        if counter < len(s) -1:
                            counter += 1
                        break
            print(tester)
            
            if tester == s:
                return True
            else:
                return False