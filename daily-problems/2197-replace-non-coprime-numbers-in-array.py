from typing import List
from math import gcd

"""
    Nothing crazy in this "hard" problem, everything is clearly mentioned in the question
"""
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for n in nums:
            stack.append(n)
            while len(stack) >= 2 and (g := gcd(stack[-1], stack[-2])) != 1:
                a, b = stack.pop(),  stack.pop()
                # LCM * GCF = product of two numbers
                lcm = a * b // g
                stack.append(lcm)
        return stack