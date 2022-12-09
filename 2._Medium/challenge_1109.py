class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """

        op = [0]*n
        cl = [0]*n
        
        for i in bookings:
            op[i[0]-1] += i[2]
            cl[i[1]-1] += i[2]
            
        ret, tmp = [0]*n, 0
        for i in range(n):
            tmp += op[i]
            ret[i] = tmp
            tmp -= cl[i]
            
        return ret