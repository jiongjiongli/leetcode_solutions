from typing import List


def calculate_exp(number, base):
    """
    Returns:
        1. Exponent of base
        2. Remaining number with all base factors removed
    """
    exp = 0

    while (number % base) == 0:
        number = number // base
        exp += 1

    return exp, number


def factorize(number, M):
    """
    Factor number into powers of 2, powers of 5, and remaining part mod `M`.
    Returns:
        1. Exponent of 2
        2. Exponent of 5
        3. Remaining part mod `M`
    """
    if number == 0:
        return (0, 0, 1)

    exp_2, number = calculate_exp(number, 2)
    exp_5, number = calculate_exp(number, 5)

    return exp_2, exp_5, number % M


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums) - 1
        M = 10
        triangular_sum = 0
        # C(n, i) % M
        cni = 1

        # Exponent of 2 and 5 in C(n, i)
        exp_2 = 0
        exp_5 = 0
        # Remaining factor after removing 2s and 5s in C(n, i)
        remain_factor = 1

        # Precompute inverses for numbers coprime with M
        # Because a / b mod M = a * inv(b) mod M if b * inv(b) = 1 mod M
        inv = [0] * M

        for number, div_inverse in [(1, 1), (3, 7), (7, 3), (9,9)]:
            inv[number] = div_inverse

        # Precompute multiplication mod M after * 2 or * 5
        remain_mult_2 = [((number * 2) % M) for number in range(M)]
        remain_mult_5 = [((number * 5) % M) for number in range(M)]

        for index, elem in enumerate(nums):
            if index > 0:
                # C(n, i) = C(n, i-1) * (n - i + 1) / i
                # Factorize numerator (n- i + 1) and denominator (i)
                mul_exp_2, mul_exp_5, mul_remain_factor = factorize(n - index + 1, M)
                div_exp_2, div_exp_5, div_remain_factor = factorize(index, M)

                # Compute factors of C(n, i) based on C(n, i-1)
                exp_2 += mul_exp_2 - div_exp_2
                exp_5 += mul_exp_5 - div_exp_5
                remain_factor = (remain_factor * mul_remain_factor * inv[div_remain_factor]) % M

                # Compute C(n, i) using factors exp_2, exp_5, remain_factor
                cni = remain_factor

                for _ in range(exp_2):
                    cni = remain_mult_2[cni]

                for _ in range(exp_5):
                    cni = remain_mult_5[cni]

            # Add current ith element multiplied by current C(n, i) mod M
            triangular_sum = (triangular_sum + elem * cni) % M

        return triangular_sum
