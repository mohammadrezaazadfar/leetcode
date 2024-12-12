class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(',
                   '}': '{',
                   ']': '['}
        for i in s:
            if i in mapping.values():
                stack.append(i)
            elif i in mapping.keys():
                if not stack or stack[-1] != mapping[i]:
                    return False
                else:
                    stack.pop()
        return not stack


s = "(){}"
x = Solution()
print(x.isValid(s))
