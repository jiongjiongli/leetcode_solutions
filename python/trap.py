# 42. Trapping Rain Water

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        stack = [0] * len(height)
        top = 0

        for index, curr_height in enumerate(height):
            start = top - 1

            while start >= 0 and height[stack[start]] < curr_height:
                start -= 1

            min_height = curr_height if start >= 0 else height[stack[0]]

            for stack_index in range(max(start, 0) + 1, top):
                result += (min_height - height[stack[stack_index]]) * (stack[stack_index] - (stack[stack_index - 1]))

            top = start + 1
            stack[top] = index
            top += 1

        return result

