# Q_05_group-anagrams.py
# 문자열 배열을 받아 애너그램 단위로 그룹핑하라.

from typing import List
import collections

input = ["eat", "tea", "tan", "ate", "nat", "bat"]

class Solution :
    def groupAnagrams(self, strs: List[str]) -> List[List[str]] :
        anagrams = collections.defaultdict(list)
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
            # sorted(str, key=str[0], str[-1]) : 기준 지정가능
        
        return list(anagrams.values())

s = Solution()
result = s.groupAnagrams(input)
print(result)


