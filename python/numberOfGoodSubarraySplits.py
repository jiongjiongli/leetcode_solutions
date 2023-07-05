class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        M = 10**9 + 7
        index = 0

        while index < len(nums) and nums[index] == 0:
            index += 1

        if index == len(nums):
            return 0

        result = 1
        prev_one_index = index
        index += 1

        while index < len(nums):
            while index < len(nums) and nums[index] == 0:
                index += 1

            if index == len(nums):
                return result

            result = (result * (index - prev_one_index)) % M
            prev_one_index = index
            index += 1

        return result
