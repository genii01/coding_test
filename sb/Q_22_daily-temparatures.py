# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
# Q_22_daily-temparatures.py
from typing import List
class Solution :
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0]*len(T)
        stack = []
        for i, cur in enumerate(T) :
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                ans[last] = i - last                
            stack.append(i)
        return ans

T = [73, 74, 75, 71, 69, 72, 76, 73]
s = Solution()
res = s.dailyTemperatures(T)
print(res)


