# Q_04_most-common-word.py

from typing import List
import re
import collections
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

class wordCounter :
    def mostCommonWord(self, paragraph:str, banned:List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]',' ',paragraph).lower().split() if word not in banned]
        counts = collections.Counter(words)
        
        return counts.most_common(1)[0][0]

wc = wordCounter()
result = wc.mostCommonWord(paragraph, banned)
print(result)


