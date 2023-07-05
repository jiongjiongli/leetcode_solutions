from typing import List


class NumberList:
    def __init__(self, numbers):
        self.numbers = numbers
        self.left = 0
        self.right = len(numbers)

    @property
    def mid_index(self):
        return (self.left + self.right - 1) // 2

    @property
    def mid_value(self):
        mid_index = self.mid_index

        if self.is_even:
            return (self.numbers[mid_index] + self.numbers[mid_index + 1]) / 2

        return self.numbers[mid_index]

    def __getitem__(self, index):
        return self.numbers[index]

    def __len__(self):
        return self.right - self.left

    @property
    def is_even(self):
        return len(self) % 2 == 0


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        numbers_dict = {
            'first': NumberList(nums1),
            'second': NumberList(nums2)
        }

        median_value = self.find_median(numbers_dict)

        return median_value

    def find_median(self,
                    numbers_dict):
        first = numbers_dict['first']
        second = numbers_dict['second']

        # len(first) = 0
        if len(first) == 0:
            return second.mid_value

        # len(second) = 0
        if len(second) == 0:
            return first.mid_value

        # len(first) = 1 and len(second) = 1
        if len(first) == 1 and len(second) == 1:
            return (first.mid_value + second.mid_value) / 2

        # len(first) = 1 and len(second) > 1
        if len(first) == 1:
            median_value = self.find_median_first_one_elem(numbers_dict)

            return median_value

        # len(first) > 1 and len(second) = 1
        if len(second) == 1:
            numbers_dict['first'] = second
            numbers_dict['second'] = first
            median_value = self.find_median_first_one_elem(numbers_dict)

            return median_value

        # First count > 1 and second count > 1

        first_spit_index = first.mid_index
        second_split_index = second.mid_index

        if not second.is_even:
            second_split_index -= 1

        first_left, first_right = first[first_spit_index:first_spit_index + 2]
        second_left, second_right = second[second_split_index:second_split_index + 2]

        if first_right < second_left:
            # first_left <= first_right < second_left <= second_right
            first_filter_out_count = first_spit_index + 1 - first.left
            second_filter_out_count = second.right - (second_split_index + 1)

            filter_out_count = min(first_filter_out_count, second_filter_out_count)
            first.left += filter_out_count
            second.right -= filter_out_count

            return self.find_median(numbers_dict)

        # first_right >= second_left

        if first_left > second_right:
            # second_left <= second_right < first_left <= first_right
            first_filter_out_count = first.right - (first_spit_index + 1)
            second_filter_out_count = second_split_index + 1 - second.left

            filter_out_count = min(first_filter_out_count, second_filter_out_count)
            first.right -= filter_out_count
            second.left += filter_out_count

            return self.find_median(numbers_dict)

        # first_right >= second_left and first_left <= second_right

        if first_left < second_left:
            # first_left < second_left <= first_right
            if first.is_even:
                # Both even
                if second.is_even:
                    return (second_left + min(first_right, second_right)) / 2

                # First even, second odd
                return min(first_right, second_right)

            if second.is_even:
                # First odd, second even
                return second_left

            # Both odd
            return (second_left + min(first_right, second_right)) / 2

        # first_right >= second_left and first_left <= second_right
        #                            and first_left >= second_left
        # So second_left <= first_left <= second_right
        if first.is_even:
            if second.is_even:
                # Both even
                return (first_left + min(first_right, second_right)) / 2

            # First even, second odd
            return min(first_right, second_right)

        # First odd, second even
        if second.is_even:
            return first_left

        # Both odd
        return (first_left + min(first_right, second_right)) / 2

    def find_median_first_one_elem(self, numbers_dict):
        first = numbers_dict['first']
        second = numbers_dict['second']

        # len(first) = 1 and len(second) > 1

        # len(second) is even
        if second.is_even:
                if first.mid_value < second[second.mid_index]:
                    return second[second.mid_index]

                return min(first.mid_value, second[second.mid_index + 1])

        # len(second) is odd

        if first.mid_value < second[second.mid_index]:
            return (max(first.mid_value, second[second.mid_index - 1]) + second[second.mid_index]) / 2

        return (min(first.mid_value, second[second.mid_index + 1]) + second[second.mid_index]) / 2
