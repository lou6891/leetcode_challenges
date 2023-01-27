'''
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        o = []
        e = 0
    
        if len(set(s)) != len(s):
            
            for i in range(len(s)):

                for c in range(i, len(s)):
                    if s[c] not in o:
                        o.append(s[c])
                        c += 1
                    else:
                        e = max(e, len(o))
                        o = []
                        break
            
            return e
            
        else:
            return len(s)
       