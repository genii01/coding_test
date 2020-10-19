# %%
# Q_20-valid-parentheses.py
# 괄호로 된 입력값이 유효한지 판별하라.

from typing import List
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

stack = Stack()

class Solution :
    def validParentheses (self, s: str) -> bool :
        table = { ')':'(', '}':'{', ']':'[' }
        for char in s :
            if char not in table :
                stack.push(char)
            elif table[char] != stack.pop() :
                return False
        return True

string = "()[]{}"
s = Solution()
print(s.validParentheses(string))


