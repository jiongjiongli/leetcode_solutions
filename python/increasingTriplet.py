from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        num_sequence = 3

        if len(nums) < num_sequence:
            return False

        dp = [None] * (num_sequence - 1)

        for number in nums:
            dp_index = 0

            if dp[dp_index] is not None and dp[dp_index] < number:
                return True

            dp_index += 1

            while dp_index < len(dp) and (not (dp[dp_index] is not None and dp[dp_index] < number)):
                dp_index += 1

            dp_index -= 1

            if not (dp[dp_index] is not None and dp[dp_index] < number):
                dp[dp_index] = number

        return False


