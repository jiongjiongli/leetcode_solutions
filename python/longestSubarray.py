# 1493. Longest Subarray of 1's After Deleting One Element
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        max_len = 0

        tail_len = 0
        tail_len_combined = 0

        is_zero_exists = False

        for number in nums:
            if number == 0:
                tail_len_combined = tail_len
                tail_len = 0

                is_zero_exists = True
                continue

            if tail_len_combined > 0:
                tail_len_combined += 1

            tail_len += 1

            max_len = max(max_len, tail_len, tail_len_combined)

        return max_len if is_zero_exists else len(nums) - 1
