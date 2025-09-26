from typing import List
"""
    Since a <= b <= c, therefore if c + {a, b} > {a, b}
    therefore the only condition that matters is a + b > c
"""
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)

        #find the smallest number that is >sum
        # every number less than that is valid
        def find(start, sum):
            l = start
            r = N - 1
            k = l - 1
            while l <= r:
                m = (l + r)//2
                if sum > nums[m]:
                    k = m
                    l = m + 1
                else:
                    r = m - 1
            return k
                
        count = 0
        for i in range(N - 2):
            for j in range(i + 1, N - 1):
                val = find(j + 1, nums[i] + nums[j]) - j
                count += val
        return count
        