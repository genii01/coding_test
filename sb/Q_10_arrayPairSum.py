# %%
# Q_10_arrayPairSum.py
# 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라.
from typing import List

class solusion :
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])

s = solusion()
input = [1,3,4,2]
print(s.arrayPairSum(input))


