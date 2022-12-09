class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        numerlas = {"I" :1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        summ = 0

        for i, v in enumerate(s):
            val = numerlas[v]
            if i < len(s) -1 and  numerlas[v] >= numerlas[s[i+1]]:
                summ += numerlas[v]
            elif i == len(s) -1:
                summ += numerlas[v]
            else:
                summ -= numerlas[v]

        return summ