# 135. Candy

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        result = 0

        left_candy = 0
        index = 0

        while index < len(ratings):
            right = index + 1

            # Move right until right value >= current.
            while right < len(ratings) and ratings[right] < ratings[right - 1]:
                right += 1

            right_candy = right - index - 1

            # No left value, or current value = left.
            if index == 0 or ratings[index] == ratings[index - 1]:
                candy = right_candy + 1
            else:
                # Current value > left.
                candy = max(left_candy, right_candy) + 1

            result += candy + right_candy * (right_candy + 1) // 2

            index = right
            left_candy = candy if right_candy == 0 else 1

        return result




