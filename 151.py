class Solution:
    def m(self, x: int) -> int:
        x = str(x)
        j = -1
        for i in range(len(x)):
            if x[i] == x[j]:
                j -= 1
            else:
                return False
        return True


b = Solution()

print(b.m(1))
