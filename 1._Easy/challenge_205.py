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
