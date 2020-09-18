from typing import List

class Solution :
    #조회 구조 개선
    def twoSum(self,nums:List[int],target:int) -> List[int]:
        nums_map = {}

        for i,num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num],i]
            nums_map[num] = i

nums = [2, 7, 11, 5]
target = 9

s = Solution()
print(s.twoSum(nums,target))