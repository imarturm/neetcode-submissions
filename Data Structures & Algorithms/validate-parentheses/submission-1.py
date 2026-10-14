class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"{": "}", "[": "]", "(": ")"}
        stack = []
        for c in s:
            if c in pairs.keys():
                stack.append(c)
            elif c in pairs.values():
                if not stack or pairs[stack.pop()] != c:
                    return False
        return not stack
