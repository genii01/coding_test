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



## 승범
def reverseString(s) :
    return s.reverse()

input_data = ["H", "a", "n", "n", "a","h"]
reverseString(input_data)
print(input_data)