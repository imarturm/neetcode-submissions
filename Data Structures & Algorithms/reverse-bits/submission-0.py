class Solution:
    def reverseBits(self, n: int) -> int:
        count = 0
        res = 0
        while n:
            bit = n & 1
            n >>= 1
            count += 1
            res += bit * 2 ** (32 - count)
        return res