"""
standard dp problem:
    for every l and r (first and last vertex of polygon),
        select any one node as midopint and triangulate it,
        after that, you have 2 polynomials with first and last as l, i and i, r
        solve for that subproblem, cache l and r
"""


from typing import List
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        minCost = 10e20 

        curCost = 0
        def dfs(arr):
            nonlocal curCost
            nonlocal minCost
            N = len(arr)
            if N <= 2:
                minCost = min(curCost, minCost)
                return

            for i in range(N):
                l = i - 1 if i - 1 >= 0 else N - 1
                r = i + 1 if i + 1 < N else 0
                curCost += arr[l] * arr[i] * arr[r]
                dfs(arr[:i] + arr[i + 1:])

        dfs(values)
        return minCost
        
