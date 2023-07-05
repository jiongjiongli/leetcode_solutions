from typing import List



class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        best_sum = sum(nums[:3])

        for index in range(len(nums) - 3 + 1):
            first_number = nums[index]

            sum_value = self.two_sum_closest(nums, index + 1, target - first_number)
            sum_value += first_number

            if abs(sum_value - target) < abs(best_sum - target):
                best_sum = sum_value

        return best_sum

    def two_sum_closest(self, nums, start_index, target):
        end_index = len(nums) - 1
        best_sum = sum(nums[start_index:start_index + 2])

        while start_index < end_index:
            sum_value = nums[start_index] + nums[end_index]

            if abs(sum_value - target) < abs(best_sum - target):
                best_sum = sum_value

            if sum_value == target:
                return sum_value

            if sum_value < target:
                start_index += 1
            else:
                end_index -= 1

        return best_sum
