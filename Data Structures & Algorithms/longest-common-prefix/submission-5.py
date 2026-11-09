class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i, column in enumerate(zip(*strs)):
            if len(set(column)) > 1:
                return strs[0][:i]
        return min(strs, key=len)