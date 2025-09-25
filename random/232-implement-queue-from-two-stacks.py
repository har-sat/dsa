"""
    to get ~O(1) i.e., amortised constant time complexity,
    push into one stack and pop from the other one,
    if the other stack is empty, pop everything from the first stack and
    add it to the second one.
"""


#HINT: when you pop from a stack and push that element to another stack,
#      the other stack has all the elements in reverse order
class MyQueue:
    def __init__(self):
        self.first = []
        self.second = []

    def _transfer(self):
        while self.first:
            self.second.append(self.first.pop())
    
    def push(self, x: int) -> None:
        self.first.append(x)

    def pop(self) -> int:
        if self.empty():
            return -1
        if self.second == []:
            self._transfer()

        return self.second.pop()

    def peek(self) -> int:
        if self.empty():
            return -1
        if self.second == []:
            self._transfer()

        return self.second[-1]
    
    def empty(self) -> bool:
        return self.first == self.second == []
