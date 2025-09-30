from typing import List
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while (N := len(nums)) > 1:
            newNums = [0]*(N - 1)
            for i in range(N - 1):
                newNums[i] = (nums[i] + nums[i + 1]) % 10
            nums = newNums
        return nums[0]

"""
    very straight forward question, should've been an easy icl
"""