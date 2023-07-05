

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if not (len(s) >= 2 and len(s) == len(goal)):
            return False

        diff_char_list = []

        for src_char, dest_char in zip(s, goal):
            if src_char != dest_char:
                diff_char_list.append((src_char, dest_char))

                if len(diff_char_list) > 2:
                    return False

        if not diff_char_list:
            char_visited = [False] * (ord('z') + 1)

            for src_char in s:
                if char_visited[ord(src_char)]:
                    return True

                char_visited[ord(src_char)] = True

            return False

        if len(diff_char_list) == 1:
            return False

        return diff_char_list[0][::-1] == diff_char_list[1]
