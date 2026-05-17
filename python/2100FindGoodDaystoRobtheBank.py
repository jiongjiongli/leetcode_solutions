class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        if time == 0:
            return list(range(len(security)))

        good_day_indices = []

        left_max = 0
        right_max = 0

        index = 1
        right_index = index + time

        while right_index < len(security):
            if security[index-1] >= security[index]:
                left_max += 1
            else:
                left_max = 0

            if security[right_index-1] <= security[right_index]:
                right_max += 1
            else:
                right_max = 0

            if left_max >= time and right_max >= time:
                good_day_indices.append(index)

            index += 1
            right_index += 1

        return good_day_indices
