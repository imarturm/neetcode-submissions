class Solution:
    def numDecodings(self, s: str) -> int:
        226

        2 + 26
        22 + 6

        2 + 6

        # 2 2 6
        # 4 2 1 0 0

        jump_one, jump_two = 1, 0
        n = len(s)
        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                jump_one, jump_two = 0, jump_one
            else:
                new_jump_one = jump_one + (0 if int(s[i:i + 2]) > 26 else jump_two)
                jump_one, jump_two = new_jump_one, jump_one
        return jump_one