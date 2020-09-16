import collections
from typing import List
import re

class Solution :
    def mostCommonWord(self,paragraph:str,banned:List[str]) -> str:
        words = [word for word in re.sub('[^\w]',' ',paragraph).lower().split()
                 if word not in banned]
        # words : ['bob', 'a', 'ball', 'the', 'ball', 'flew', 'far', 'after', 'it', 'was']
        counts = collections.Counter(words)
        # counts : Counter({'ball': 2, 'bob': 1, 'a': 1, 'the': 1, 'flew': 1, 'far': 1, 'after': 1, 'it': 1, 'was': 1})
        return counts.most_common(1)[0][0] # counts.most_common(1) : [('ball', 2)]

paragraph = 'Bob hit a ball, the hit BALL flew far after it was hit.'
banned = ["hit"]
s = Solution()
print(s.mostCommonWord(paragraph,banned))