class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        if k == 1:
            return n

        if n == 1:
            return 1

        K = k + 1
        M = n + 1

        dp = [([0] * M) for _ in range(K)]

        for m in range(1, M):
            dp[1][m] = m

        for k in range(1, K):
            dp[k][1] = 1

        for m in range(2, M):
            for k in range(2, K):
                dp[k][m] = dp[k - 1][m - 1] + 1 + dp[k][m - 1]

            if dp[k][m] >= n:
                return m

        return -1
