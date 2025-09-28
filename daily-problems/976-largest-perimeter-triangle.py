from typing import List

#sort the array
#find the largest valid triangle, return it
# you don't have to check with every side length when you sort the array,
# if nums[i + 1] + num[i + 2] > nums[i] is false, then there are no numbers that can satisfy, as every other number will be smaller than nums[i + 2]
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        N = len(nums)

        for i in range(N - 2):
            s = nums[i + 1] + nums[i + 2]
            if s > nums[i]:
                return s + nums[i]
        return 0
