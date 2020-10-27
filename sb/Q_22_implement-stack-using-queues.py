# %%
# Q_22_implement-stack-using-queues.py
# 큐를 이용하여 다음 연산을 지원하는 스택을 구현하라.
import collections
from typing import List

class Solution :
    def __init__(self):
        self.q = collections.deque()

    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())
    def pop(self):
        return self.q.popleft()
    def top(self):
        return self.q[0]
    def empty(self):
        return len(self.q) == 0

s = Solution()
s.push(1)
s.push(2)
print(s.empty())
print(s.pop())
print(s.pop())
