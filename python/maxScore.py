# 1423. Maximum Points You Can Obtain from Cards

from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        nums = cardPoints
        right = len(nums) - k
        max_score = k_sum = sum(nums[right:])

        for left in range(k):
            k_sum += nums[left] - nums[right]

            max_score = max(max_score, k_sum)

            right += 1

        return max_score
