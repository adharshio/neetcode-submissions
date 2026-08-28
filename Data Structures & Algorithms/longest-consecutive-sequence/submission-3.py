class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxLen = 0
        for i in nums:
            curLen = 0
            if i - 1 not in nums:
                stNum = i
                while stNum in nums:
                    curLen += 1
                    stNum += 1
                maxLen = max(maxLen,curLen)
            
        return maxLen
         