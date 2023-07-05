class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        t_char_freqs = [0] * (ord('z') + 1)

        for char in t:
            t_char_freqs[ord(char)] += 1

        s_char_freqs = [0] * (ord('z') + 1)

        matched_char_count = 0
        left = 0
        right = 0

        # Find a window [left, right) that convers t.
        while right < len(s) and matched_char_count != len(t):
            char_ord = ord(s[right])
            s_char_freqs[char_ord] += 1

            if s_char_freqs[char_ord] <= t_char_freqs[char_ord]:
                matched_char_count += 1

            right += 1

        # If no matched window, then return empty string.
        if matched_char_count != len(t):
            return ""

        best_window = (left ,right)

        while left < len(s):
            # Now we have a new matched window.
            # Slide left forward for more matches.
            while s_char_freqs[ord(s[left])] > t_char_freqs[ord(s[left])]:
                char_ord = ord(s[left])
                s_char_freqs[char_ord] -= 1
                left += 1

            if right - left < best_window[1] - best_window[0]:
                best_window = (left, right)

            # Slide left, then the window is mismatched.
            missing_char = s[left]
            s_char_freqs[ord(missing_char)] -= 1
            left += 1

            # Slide right until the missing char appears.
            while right < len(s) and s[right] != missing_char:
                char_ord = ord(s[right])
                s_char_freqs[char_ord] += 1
                right += 1

            if right >= len(s):
                return s[best_window[0]: best_window[1]]

            # Slide right, then the window is matched.
            char_ord = ord(missing_char)
            s_char_freqs[char_ord] += 1
            right += 1

        return s[best_window[0]: best_window[1]]
