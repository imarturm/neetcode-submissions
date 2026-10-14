class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = longest = 0
        window = {}
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            while sum(window.values()) - max(window.values()) > k:
                window[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest