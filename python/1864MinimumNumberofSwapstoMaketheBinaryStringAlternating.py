class Solution:
    def minSwaps(self, s: str) -> int:
        # count '0' at position 0, 2, ...
        even_pos_num_0 = 0
        # count '0' at position 1, 3, ...
        odd_pos_num_0  = 0

        idx = 0

        while idx < len(s):
            if s[idx] == '0':
                even_pos_num_0 += 1

            idx += 1

            if idx < len(s) and s[idx] == '0':
                odd_pos_num_0 += 1
            
            idx += 1
            
        # count '1' at position 0, 2, ...
        even_pos_num_1 = (len(s) + 1) // 2 - even_pos_num_0
        # count '1' at position 1, 3, ...
        odd_pos_num_1  = (len(s)) // 2 - odd_pos_num_0

        num_swap = -1

        if even_pos_num_0 == odd_pos_num_1:
            # Swap 0 at even_pos with 1 at odd_pos
            num_swap = even_pos_num_0

        if even_pos_num_1 == odd_pos_num_0:
            # Swap 1 at even_pos with 10 at odd_pos
            if num_swap == -1:
                num_swap = even_pos_num_1
            else:    
                num_swap = min(num_swap, even_pos_num_1)

        return num_swap
