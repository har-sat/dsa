from sortedcontainers import SortedList # pyright: ignore[reportMissingImports]
from collections import defaultdict
from typing import List

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.highest = defaultdict(SortedList)
        self.hash = {}

        for (f, c, r) in zip(foods, cuisines, ratings):
            self.hash[f] = (-r, c)
            self.highest[c].add((-r, f))

    def changeRating(self, f: str, newRating: int) -> None:
        r, c = self.hash[f]
        self.hash[f] = (-newRating, c)

        self.highest[c].remove((r, f))       
        self.highest[c].add((-newRating, f))

    def highestRated(self, c: str) -> str:
        return self.highest[c][0][1]
