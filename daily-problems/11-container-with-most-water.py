from typing import List

"""
Pretty self explanatory and standard two pointer problem
"""
class Solution:
    def containerWithMostWater(height: List[int]):
        N = len(height)

        maxArea = 0
        l = 0
        r = N - 1
        while l < r:
            h = min(height[l], height[r])
            maxArea = max(maxArea, h * (r - l))

            if h == height[l]:
                l += 1
            else:
                r -= 1
        return maxArea
