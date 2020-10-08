from typing import List

class Solution :
    def dailyTemperatures(self, T:List[int]) -> List[int]:
        answer = [0] * len(T)
        stack = []

        for i,cur in enumerate(T):
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
                #[1,1,4,2,1,1,0,0]
            stack.append(i) #6 7
        return answer

temperatures = [73,74,75,71,69,72,76,73]
s = Solution()
result = s.dailyTemperatures(temperatures)
print(result)