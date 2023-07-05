from typing import List
import math


class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        digit_counts = [0] * 10

        beautiful_pair_count = 0

        for number in nums:
            last_digit = number % 10

            for first_digit, digit_count in enumerate(digit_counts):
                if self.gcd(first_digit, last_digit) == 1:
                    beautiful_pair_count += digit_count

            first_digit = self.get_first_digit(number)

            digit_counts[first_digit] += 1

        return beautiful_pair_count

    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b

        return a

    def get_first_digit(self, number):
        while number >= 10:
            number = number // 10

        return number

    def generate_primes(self, max_number):
        is_composite = [False] * (max_number + 1)

        for index in range(2, math.floor(math.sqrt(max_number)) + 1):
            for next_index in range(index**2, len(is_composite), index):
                is_composite[next_index] = True

        primes = [index for index, is_composite_number in enumerate(is_composite)
                  if index > 1 and (not is_composite_number)]
        return primes

    def is_coprime(self, number, next_number, primes):
        for prime in primes:
            if ((number % prime) == 0) and ((next_number % prime) == 0):
                return False

        return True


def main():
    solution = Solution()

    input_data = [31,25,72,79,74]
    print(solution.countBeautifulPairs(input_data))


if __name__ == '__main__':
    main()
