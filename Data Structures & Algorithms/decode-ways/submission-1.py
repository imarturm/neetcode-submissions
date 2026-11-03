class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        jump_one, jump_two = 1, 0
        for i in range(n - 1, -1, -1):
            new_jump_one = jump_one
            if s[i] == "0":
                new_jump_one = 0
            elif int(s[i:i + 2]) <= 26:
                new_jump_one += jump_two
            jump_one, jump_two = new_jump_one, jump_one
        return jump_one