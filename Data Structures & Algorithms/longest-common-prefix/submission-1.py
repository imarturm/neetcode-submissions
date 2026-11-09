class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []
        for i, c in enumerate(strs[0]):
            if not all(len(s) > i and s[i] == c for s in strs[1:]):
                return "".join(prefix)
            prefix.append(c)
        return "".join(prefix)