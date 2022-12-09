class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 5:
            return 0

        else :

            c = 0
            while(n >= 5):
                n //= 5
                c += n

            return c        