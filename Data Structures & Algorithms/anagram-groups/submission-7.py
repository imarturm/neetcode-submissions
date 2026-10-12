class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            count = ''.join(sorted(s))
            groups.setdefault(count, []).append(s)
        return list(groups.values())