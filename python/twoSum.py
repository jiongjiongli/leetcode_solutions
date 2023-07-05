class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_index_dict = dict()

        for index, number in enumerate(nums):
            matched_number = target - number
            if matched_number in number_index_dict:
                return [number_index_dict[matched_number], index]

            number_index_dict[number] = index

        return None
