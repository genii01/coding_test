# %%
# Q_11_product-of-array-except-self.py
# 배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라.
from typing import List

class solusion :
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums = [1,2,3,4]
        res = []
        p = 1
        for i in range(0, len(nums)):
            res.append(p)
            p = p * nums[i]
        p = 1
        for i in range(0, len(nums)):
            res[-i-1] = res[-i-1]*p
            p = p*nums[-i-1]
        return res

s = solusion()
input = [1,2,3,4]
print(s.productExceptSelf(input))


