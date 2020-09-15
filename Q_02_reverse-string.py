## 준영
input_data = "hello"
# ['h', 'e', 'l', 'l', 'o'] 생성
input_data = list(input_data)

def reverseString(s):
    left, right = 0, len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s

result = reverseString(input_data)
print(result)

## 영보

from typing import List

class Solution :
    def reverseString(self,s:List[str]) -> None:
        s.reverse()
        print(s)

sample = ['a','b','c','d','e']
s = Solution()
s.reverseString(sample)
