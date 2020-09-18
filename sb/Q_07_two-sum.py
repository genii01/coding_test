# %%
#Q_07_two_sum.py
# 덧셈하여 타겟을 만들 수 있는 배열의 두숫자 인덱스를 리턴하라.
from typing import List

class Solution :
    def twoSum(self, nums: List[int], target: int) -> List[int] :
        for i in range(len(nums)) :
            for j in range(i+1, len(nums)) :
                if nums[i] + nums[j] == target :
                    return [i, j]
    
    def twoSum2(self, nums: List[int], target: int) -> List[int] :
        nums_map = {}
        for i, num in enumerate(nums) :
            nums_map[num] = i
        for i, num in enumerate(nums) :
            if target - num in nums_map and i != nums_map[target-num]:
                return [nums.index(num), nums_map[target-num]]

nums = [2, 7, 11, 15]
target = 9

s = Solution()
result = s.twoSum(nums, target)
result2 = s.twoSum2(nums, target)
print(result)
print(result2)
