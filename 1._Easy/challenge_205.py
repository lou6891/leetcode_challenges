'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
'''

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s = list(s)
        t = list(t)

        ss = sorted(set(s), key=s.index)
        ts = sorted(set(t), key=t.index)
        d = {}
        t2 = []

        if (len(ss) == len(ts)):
            

            for i in range(len(ss)):
                d[ss[i]] = ts[i]
            
            for i in s:
                t2.append(d[i])
            
            print(t2)

            if t2 == t:
                return True


        else:
            return False
