class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxArea = 0
        while l < r:
            width = r - l 
            height = min(heights[l],heights[r])
            curArea = width * height
            maxArea = max(maxArea,curArea)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxArea