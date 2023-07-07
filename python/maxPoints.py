from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        num_max_points = 1

        for index, first_point in enumerate(points):
            intercept_dict = {}

            for second_point in points[index + 1:]:
                x_diff = second_point[0] - first_point[0]
                y_diff = second_point[1] - first_point[1]

                intercept = self.get_intercept(x_diff, y_diff)

                intercept_dict.setdefault(intercept, 0)
                intercept_dict[intercept] += 1

                num_max_points = max(num_max_points, intercept_dict[intercept] + 1)

        return num_max_points

    def get_intercept(self, x, y):
        if x == 0:
            return (0, 1)

        if y == 0:
            return (1, 0)

        if x < 0:
            x = -x
            y = -y

        m = gcd(abs(x), abs(y))

        return (x // m, y // m)

    def gcd(self, x, y):
        while y != 0:
            x, y = y, x % y

        return x
