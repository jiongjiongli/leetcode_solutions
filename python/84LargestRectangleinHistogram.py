from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        num_elems = len(heights)
        left  = [0] * num_elems
        max_area = 0

        for idx in range(num_elems):
            height = heights[idx]
            left_idx = idx - 1

            while left_idx >= 0 and heights[left_idx] >= height:
                area = heights[left_idx] * (idx - left[left_idx] - 1)
                max_area = max(max_area, area)

                left_idx = left[left_idx]

            left[idx] = left_idx

        idx = num_elems
        left_idx = num_elems - 1

        while left_idx >= 0:
            area = heights[left_idx] * (idx - left[left_idx] - 1)
            max_area = max(max_area, area)

            left_idx = left[left_idx]

        return max_area
