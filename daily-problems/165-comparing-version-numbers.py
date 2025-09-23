"""
    shit is so easy
"""
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        a, b = version1.split('.'), version2.split('.')
        N = max(len(a), len(b))

        if N - len(a) > 0:
            a.extend([0] * (N - len(a)))
        elif N - len(b) > 0:
            b.extend([0] * (N - len(b)))

        for v1, v2 in zip(a, b):
            v1 = int(v1)
            v2 = int(v2)
            if v1 > v2:
                return 1
            if v1 < v2:
                return -1
        return 0


