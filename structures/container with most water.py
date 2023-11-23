class Solution:
    def maxArea(self, height: List[int]) -> int:
        size = len(height)
        maxArea = 0
        i = 0
        j = size - 1
        while i < j:
            area = min(height[i], height[j]) * (j - i)
            if maxArea < area: maxArea = area
            if height[i] < height[j]: i += 1
            else: j -= 1
        return maxArea
