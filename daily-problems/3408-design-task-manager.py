from sortedcontainers import SortedList # type: ignore
from typing import List
"""
    This is the same thing as yesterday bro wtf
"""
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.tasks = SortedList()
        self.users = {}
        self.priority = {}
        for (userId, taskId, priority) in tasks:
            self.add(userId, taskId, priority)
    
    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.users[taskId] = userId
        self.priority[taskId] = priority
        self.tasks.add((priority, taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        oldPriority = self.priority[taskId]
        self.tasks.remove((oldPriority, taskId))

        self.priority[taskId] = newPriority
        self.tasks.add((newPriority, taskId))
        

    def rmv(self, taskId: int) -> None:
        self.users.pop(taskId)
        priority = self.priority.pop(taskId)
        self.tasks.remove((priority, taskId))
        

    def execTop(self) -> int:
        if len(self.tasks) == 0:
            return -1

        _, taskId = self.tasks[-1]
        user = self.users[taskId]
        self.rmv(taskId)
        return user
        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)