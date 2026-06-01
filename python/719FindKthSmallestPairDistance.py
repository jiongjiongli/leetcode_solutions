class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        left = 0
        right = nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2
            num_pairs = self.count_pairs(nums, mid)

            if num_pairs < k:
                left = mid + 1
            else:
                right = mid

        return left

    def count_pairs(self, nums, max_diff):
        num_pairs = 0
        right_index = 0

        for left_index, number in enumerate(nums):
            while right_index < len(nums) and nums[right_index] - number <= max_diff:
                right_index += 1

            num_pairs += right_index - left_index - 1

        return num_pairs