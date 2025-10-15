class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        N = len(nums)
        boundaries = [0]
        for i in range(1, N):
            if not (nums[i] > nums[i - 1]):
                boundaries.append(i)
        boundaries.append(N)

        k = 0
        for i in range(len(boundaries) - 1):
            s = boundaries[i]
            e = boundaries[i + 1]

            # within subarray
            curLen = e - s
            k = max(k, curLen //2)

            # adjacent subarray
            if i + 2 < len(boundaries):
                e2 = boundaries[i + 2]
                nextLen = e2 - e 
                k = max(k, min(curLen, nextLen))

        return k
   