class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bit_number = 1
        number = 0

        for bit_position in range(32):
            bit_exists = self.one_bit_exists(nums, bit_number)

            if bit_exists:
                number = (number | bit_number)

            bit_number = (bit_number << 1)

            if bit_position == 32 - 1 and bit_exists:
                number = number - bit_number
        return number

    def one_bit_exists(self, nums, bit_number):
        zero_count = 0

        for number in nums:
            if (number & bit_number) == 0:
                zero_count += 1

        return (zero_count % 3 == 0)
