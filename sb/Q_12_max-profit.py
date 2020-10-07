
# Q_12_max-profit.py
# 한 번의 거래로 낼 수 있는 최대 이익을 산출하라.
from typing import List
import sys

class solution :
    def maxProfit(self, nums: List[int]) -> int:
        min_price = sys.maxsize
        profit = 0
        for price in nums :
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        
        return profit

nums = [7,1,5,3,6,4]
s = solution()
result = s.maxProfit(nums)
print(result)


