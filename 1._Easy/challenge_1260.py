'''
Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.

 

Example 1:

Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]
'''

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        n = len(grid)
        llen = len(grid[0])
        temp = []
        out = []

        


        for line in grid:
            for i in line:
                temp.append(i)

        
        
        def rotate(l, n):
            for i in range(n):
                l =  l[-1:] + l[:-1]
            return l

        temp = rotate(temp, k)

        while n > 0:
            a = []
            for i in range(llen):
                a.append(temp[0])
                temp.pop(0)
            out.append(a)
            n -= 1
        
        return out
