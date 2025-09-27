from typing import List
class Solution:
    # Can't use herons formula(because of floating point precision errors)
    # use determinant method to find area of triangle(shoelace method)
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        N = len(points)
        maxArea = -1

        def findArea(p1, p2, p3):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3
        
            det = x1 * (y2 - y3) - y1 * (x2 - x3) + (x2 * y3 - x3 * y2)
            area = 0.5 * abs(det)
            return area
        
        for i in range(N - 2):
            for j in range(i + 1, N - 1):
                for k in range(j + 1, N):
                    maxArea = max(maxArea, findArea(points[i], points[j], points[k]))
        return maxArea
