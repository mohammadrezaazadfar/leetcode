# 13. Roman to Integer

class Solution:
    def RomanToInt(self, s: str) -> int:
        s = list(s)
        romanNumbers = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        total = 0
        f_value = 0

        for i in reversed(s):
            if romanNumbers[i] >= f_value:
                total += romanNumbers[i]
            else:
                total -= romanNumbers[i]
            f_value = romanNumbers[i]
        return total
