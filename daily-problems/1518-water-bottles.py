from typing import List

# self explanatory code
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty = drank = numBottles
        while empty >= numExchange:
            next = empty // numExchange
            empty = next + empty % numExchange
            drank += next
        return drank
