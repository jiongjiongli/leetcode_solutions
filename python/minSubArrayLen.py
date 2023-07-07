# 209. Minimum Size Subarray Sum

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        number_sum = 0
        min_size = len(nums)

        while True:
            while right < len(nums) and number_sum < target:
                number_sum += nums[right]
                right += 1

            if number_sum < target:
                return 0 if left == 0 else min_size

            while number_sum >= target:
                min_size = min(min_size, right - left)
                number_sum -= nums[left]
                left += 1

        return 0
