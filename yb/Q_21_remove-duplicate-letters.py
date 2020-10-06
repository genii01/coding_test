import collections

class Solution :
    def removeDuplicateLtters(self, s:str) -> str:
        counter, seen, stack = collections.Counter(s),set(),[]
        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            while stack and char < stack[-1] and counter[stack[-1]] > 0 :
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)
        return ''.join(stack)

txt = 'cbacdcbc'
s = Solution()
result = s.removeDuplicateLtters(txt)
print(result)