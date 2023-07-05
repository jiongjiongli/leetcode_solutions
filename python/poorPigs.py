from typing import List
import math
import sys


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        base = (minutesToTest // minutesToDie) + 1
        logit = math.log(buckets) / math.log(base)
        k = math.ceil(logit)

        # Fix bug: buckets = 125, base = 5, k = 3.0000000000000004
        round_value = round(logit)

        if buckets <= base** round_value:
            k = round_value

        return k
