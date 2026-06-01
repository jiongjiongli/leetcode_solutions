class Solution:
    def get_number_length(self, number):
        if number == 0:
            return 1

        length = 0

        while number != 0:
            length += 1
            number = number // 10

        return length

    def construct_seq_digit(self, first_number, number_length):
        #  1234 = (((1 * 10) + 2) * 10 + 3) * 10 + 4
        seq_digit = 0
        curr_digit = first_number

        for _ in range(number_length):
            seq_digit =  seq_digit * 10 + curr_digit
            curr_digit += 1

        return seq_digit

    def get_seq_digits(self, number_length):
        seq_digits = []

        min_first_number = 1
        # Example: number_length = 3 -> max_first_number= 9 - 3 + 1 = 7, so seq = 789
        max_first_number = 9 - number_length + 1

        for first_number in range(min_first_number, max_first_number + 1):
            seq_digit = self.construct_seq_digit(first_number, number_length)
            seq_digits.append(seq_digit)

        return seq_digits

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        low_length = self.get_number_length(low)
        high_length = self.get_number_length(high)
        high_length = min(high_length, 9)

        seq_digits = []

        for number_length in range(low_length, high_length + 1):
            digits = self.get_seq_digits(number_length)
            
            for seq_digit in digits:
                if low <= seq_digit <= high:
                    seq_digits.append(seq_digit)

        return seq_digits