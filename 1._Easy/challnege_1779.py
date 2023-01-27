'''
You are given two integers, x and y, which represent your current location on a Cartesian grid: (x, y). You are also given an array points where each points[i] = [ai, bi] represents that a point exists at (ai, bi). A point is valid if it shares the same x-coordinate or the same y-coordinate as your location.

Return the index (0-indexed) of the valid point with the smallest Manhattan distance from your current location. If there are multiple, return the valid point with the smallest index. If there are no valid points, return -1.

The Manhattan distance between two points (x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2).

 

Example 1:

Input: x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
Output: 2
Explanation: Of all the points, only [3,1], [2,4] and [4,4] are valid. Of the valid points, [2,4] and [4,4] have the smallest Manhattan distance from your current location, with a distance of 1. [2,4] has the smallest index, so return 2.
'''

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:

        min_dist = {
            "m_d" : 9*10**4,
            "point" : [],
            "index" : None
        }
        
        for i,point in enumerate(points):
            
            if point[0] == x or point[1] == y:
                
                md =abs(x - point[0]) + abs(y - point[1])
                
                if md < min_dist["m_d"]:
                    min_dist["m_d"] = md
                    min_dist["point"] = point
                    min_dist["index"] = i            
            else:
                continue

        
        print(min_dist)
        #print(abs(x - min_dist["point"][0]) + abs(y - min_dist["point"][1]))


        if len(min_dist["point"]) == 0:
            return -1
        else:
            return min_dist["index"]