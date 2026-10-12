class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f'{len(s)}^{s}')
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = s.find('^', i)
            count = int(s[i:j])
            res.append(s[j + 1:j + count + 1])
            i = j + 1 + count
        
        return res