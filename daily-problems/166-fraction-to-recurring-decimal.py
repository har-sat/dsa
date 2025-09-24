"""
    sort of the non fractional part first, then add a dot.
    - Use a hash map, where key: val is remainder: index it appears first
    - if the remainder is already hashed, we found a recurring part, so just enclose it with paranthesis
    - else, set seen[rem] = current len of res(which is the index of the current remainder 
        - multiply the remainder by 10(to be able to divide by the divisor)
        - divide by divisor, add quotient to ans, set rem = (rem*10) % D
    - repeat this till rem == 0
"""
class Solution:
    def fractionToDecimal(self, N: int, D: int) -> str:
        if N == 0:
            return "0"

        res = []
        if (N > 0) ^ (D > 0):
            res.append("-")

        N = abs(N)
        D = abs(D)
        res.append(str(N // D))
        if N % D == 0:
            return "".join(res)

        res.append(".")
        seen = {}
        rem = N % D
        while rem:
            print(rem)
            if rem in seen:
                res.insert(seen[rem], "(")
                res.append(")")
                break

            seen[rem] = len(res)
            
            rem *= 10
            res.append(str(rem // D))
            rem = rem % D 

        return "".join(res)

