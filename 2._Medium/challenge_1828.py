'''
You are given an array points where points[i] = [xi, yi] is the coordinates of the ith point on a 2D plane. Multiple points can have the same coordinates.

You are also given an array queries where queries[j] = [xj, yj, rj] describes a circle centered at (xj, yj) with a radius of rj.

For each query queries[j], compute the number of points inside the jth circle. Points on the border of the circle are considered inside.

Return an array answer, where answer[j] is the answer to the jth query.

Input: points = [[1,3],[3,3],[5,3],[2,2]], queries = [[2,3,1],[4,3,1],[1,1,2]]
Output: [3,2,2]
Explanation: The points and circles are shown above.
queries[0] is the green circle, queries[1] is the red circle, and queries[2] is the blue circle.

'''

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:

        out = []

        for i in queries:
            o = 0
            for p in points:
                if (p[0] - i[0])**2 + (p[1] - i[1])**2 == i[2]**2:
                    o += 1
                
                if sqrt((p[0] - i[0])**2 + (p[1] - i[1])**2) < i[2]:
                    o += 1
            out.append(o)

        return out