from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = Counter(t)
        missing = len(t)
        left = 0
        start = 0
        end = 0
        result = ""

        for right, char in enumerate(s):
            if need[char] > 0:
                missing -= 1
            need[char] -= 1

            if missing == 0:
                while need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                window = s[left:right + 1]
                if not result or len(window) < len(result):
                    result = window

                need[s[left]] += 1
                missing += 1
                left += 1

        return result
