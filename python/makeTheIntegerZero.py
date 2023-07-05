

class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1, 42 + 1):
            target = num1 - k * num2

            if target < k:
                return -1

            if target.bit_count() <= k:
                return k

        return -1
