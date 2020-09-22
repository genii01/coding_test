# %%
# Q_09_three-sum.py
# 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라.
from typing import List

nums=[-1, 0, 1, 2, -1, -4]

class solution :
    def threeSum(self, nums: List[int]) -> List[List[int]] :
        results = []
        nums.sort()

        for i in range(len(nums) - 2) :
            if i > 0 and nums[i] == nums[i -1] :
                continue
            left, right = i + 1, len(nums) - 1
            while left < right :
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0 :
                    left += 1
                elif sum > 0 :
                    right -= 1
                else :
                    results.append((nums[i], nums[left], nums[right]))
                    # i번째에서 정답을 찾은 후, left와 right가 같은 경우 스킵 
                    # [-1 0 1 -2 2 1 1 1]의 경우 right가 오른쪽 3번째 1로 이동
                    while left > right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return results
    
s = solution()
results = s.threeSum(nums)
print(results)


