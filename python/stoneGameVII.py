from typing import List
import numpy as np


class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        num_stones = len(stones)

        # Diff in alice round at subsequence [start_index, end_index]
        dp = [[0] * num_stones for _ in range(num_stones)]

        for start_index in reversed(range(num_stones - 1)):
            end_index = start_index + 1
            dp[start_index][end_index] = max(stones[start_index], stones[end_index])

            for end_index in range(start_index + 2, num_stones):
                dp[start_index][end_index] = self.alice_round(stones, dp, start_index, end_index)

        return dp[0][num_stones - 1]

    def alice_round(self, stones, dp, start_index, end_index):
        # Alice throws stone start_index, then remains [start_index + 1, end_index]
        diff_throw_first = self.bob_round(stones, dp, start_index + 1, end_index)

        # Alice throws stone end_index, then remains [start_index, end_index - 1]
        diff_throw_last  = self.bob_round(stones, dp, start_index, end_index - 1)

        return max(diff_throw_first, diff_throw_last)

    def bob_round(self, stones, dp, start_index, end_index):
        # Bob throws stone start_index, then remains [start_index + 1, end_index]
        diff_throw_first = stones[start_index] + dp[start_index + 1][end_index]

        # Bob throws stone end_index, then remains [start_index, end_index - 1]
        diff_throw_last = stones[end_index] + dp[start_index][end_index - 1]
        return min(diff_throw_first, diff_throw_last)
