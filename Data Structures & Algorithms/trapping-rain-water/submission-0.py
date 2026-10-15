class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if not n:
            return -1


        area = 0
        l = 0
        r = len(height) - 1
        maxLeft = height[l]
        maxRight = height[r]

        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft,height[l])
                area += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight,height[r])
                area += maxRight - height[r]
        return area
