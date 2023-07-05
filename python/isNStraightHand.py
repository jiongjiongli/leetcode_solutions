from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        nums = hand
        k = groupSize

        if (len(nums) % k) != 0:
            return False

        nums.sort()

        number_freq = [0] * len(nums)
        freq_index = 0

        number_index = 0

        while number_index < len(nums):
            number = nums[number_index]
            freq = 1
            number_index += 1

            while number_index < len(nums) and nums[number_index] == number:
                freq += 1
                number_index += 1

            nums[freq_index] = number
            number_freq[freq_index] = freq

            freq_index += 1

        number_count = freq_index

        for index in range(number_count):
            freq = number_freq[index]

            if freq == 0:
                continue

            number = nums[index]
            number_index = 0

            for freq_index in range(index, index + k):
                if nums[freq_index] != number or number_freq[freq_index] < freq:
                    return False

                number_freq[freq_index] -= freq
                number += 1

        return True
