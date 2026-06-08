
class Solution:
    def numberOfWays(self, s: str) -> int:
        # 0, 1, 01, 10
        num_0    = 0
        num_1    = 0
        num_01   = 0
        num_10   = 0
        # 010, 101
        num_ways = 0

        for c in s:
            if c == '0':
                num_0    += 1
                num_10   += num_1
                num_ways += num_01
            else:
                # c == '1'
                num_1    += 1
                num_01   += num_0
                num_ways += num_10

        return num_ways
