# %%
# Q_21-remove-duplicate-letters.py
# 중복된 문자를 제외하고 사전식 순서로 나열하라.
from typing import List
import collections

class Solution :
    def removeDuplicatesLetters (self, s: str) -> str :
        counter, stack, seen = collections.Counter(s), [], set()
        print(counter)
        for char in s :
            counter[char] -= 1
            if char in seen :
                continue

            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)
        return ''.join(stack)

string = "bcabc"
s = Solution()
print(s.removeDuplicatesLetters(string))


# %%
class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next
class Stack:
    def __init__(self) :
        self.last = None
    def push(self, item):
        self.last = Node(item, self.last)
    def pop(self):
        item = self.last.item
        self.last = self.last.next
        return item


