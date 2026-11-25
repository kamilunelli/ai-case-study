from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""

        need = Counter(t)
        missing = len(t)
        left = 0
        best_start = 0
        best_len = len(s) + 1

        for right, char in enumerate(s):
            if need[char] > 0:
                missing -= 1
            need[char] -= 1

            if missing == 0:
                while need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                window_len = right - left + 1
                if window_len < best_len:
                    best_len = window_len
                    best_start = left

                need[s[left]] += 1
                missing += 1
                left += 1

        return "" if best_len > len(s) else s[best_start : best_start + best_len]