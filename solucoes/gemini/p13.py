from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            h_left = height[left]
            h_right = height[right]
            if h_left < h_right:
                area = h_left * (right - left)
                left += 1
            else:
                area = h_right * (right - left)
                right -= 1
            if area > max_water:
                max_water = area

        return max_water