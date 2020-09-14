# 준영
import re
def isPalindrome(s):
    s = s.lower()

    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]

input_data = " A man, a plan, a canal : Panama"

result = isPalindrome(input_data)
print(result)

# 영보 - start!
#팰린드롬 : 앞뒤가 똑같은 단어나 문장
import re

class Solution :
    def isPalindrom(self,s:str) -> bool:
        s = s.lower()
        #정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]','',s)
        return s == s[::-1]

sample = 'A man, a plan, a canal: Panama'
s = Solution()
print(s.isPalindrom(sample))

# 승범
def isPalindrome(input) :
    strList = []
    for i in input:
        if i.isalnum() :
            strList.append(i.lower())
            
    return strList == strList[::-1]
    
input = "A man, a plan, a canal: Panama"

print(isPalindrome(input))