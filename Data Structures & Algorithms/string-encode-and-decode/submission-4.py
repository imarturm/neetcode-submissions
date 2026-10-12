class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for str in strs:
            res.append(f'{len(str)}^{str}')
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            count = []
            while s[i] != '^':
                count.append(s[i])
                i += 1
            count = int(''.join(count))
            res.append(s[i + 1:i + count + 1])
            i = i + count + 1
        
        return res