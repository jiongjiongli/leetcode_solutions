from typing import List

class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        max_sum_books = 0

        left = [0] * len(books)

        for idx, num_books in enumerate(books):
            left_idx = idx - 1

            while left_idx >= 0 and books[left_idx] - left_idx >= num_books - idx:
                left_idx = left[left_idx]

            left[idx] = left_idx

        dp = [0] * len(books)

        for idx, num_books in enumerate(books):
            left_idx = left[idx]
            left_num_books = num_books - (idx - left_idx - 1)

            if left_num_books < 0:
                dp[idx] = num_books * (num_books + 1) // 2
                continue

            dp[idx] = (left_num_books + num_books) * (idx - left_idx) // 2

            if left_idx >= 0:
                dp[idx] += dp[left_idx]

            max_sum_books = max(max_sum_books, dp[idx])

        return max_sum_books

# Test cases
tests = [
    # Official examples
    ([8,5,2,7,9], 19),
    ([7,0,3,4,5], 12),
    ([8,2,3,7,3,4,0,1,4,3], 13),

    # Single shelf
    ([1], 1),
    ([5], 5),
    ([0], 0),

    # Increasing
    ([1, 2, 3], 6),      # take all
    ([1, 2, 3, 4], 10),  # take all

    # Decreasing
    ([4, 3, 2, 1], 5),
    ([5, 4, 3, 2, 1], 7),

    # All same
    ([1, 1, 1], 1),
    ([2, 2, 2], 3),      # 1 + 2
    ([3, 3, 3], 6),      # 2 + 3

    # Contains zeros
    ([0, 0, 0], 0),
    ([0, 1, 2], 3),
    ([2, 0, 2], 2),

    # Small custom cases
    ([2, 3], 5),
    ([3, 2], 3),
    ([3, 1, 3], 4),
    ([1, 3, 5], 9),
    ([5, 3, 1], 5),

    # Peak in the middle
    ([1, 2, 10, 2, 1], 13),

    # Large plateau
    ([10, 10, 10, 10], 34),  # 7+8+9+10

    # Another easy-to-check case
    ([1, 5, 6], 12),  # 1+5+6
]

sol = Solution()

for books, expected in tests:
    result = sol.maximumBooks(books)

    print(
        f"books={books}\n"
        f"result={result}, expected={expected}, "
        f"{'PASS' if result == expected else 'FAIL'}\n"
    )

    assert result == expected, (
        f"books={books}, expected={expected}, got={result}"
    )

print("All tests passed!")
