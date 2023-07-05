from typing import List


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        max_score = 0
        sum_value = 0
        queue = [0] * 3
        head = 0

        for stone_value in stoneValue[::-1]:
            sum_value += stone_value
            max_score = sum_value - min(queue)

            head = (head + 1) % len(queue)
            queue[head] = max_score

        if max_score * 2 == sum_value:
            return 'Tie'

        if max_score * 2 > sum_value:
            return 'Alice'

        return 'Bob'
