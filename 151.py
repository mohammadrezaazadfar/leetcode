class Solution:
    def is_palindrome(self, x: int) -> bool:
        x = str(x)

        for i in range(len(x) // 2):
            if x[i] != x[-(i + 1)]:
                return False

        return True
test  = Solution()

print(test.is_palindrome(123565321))