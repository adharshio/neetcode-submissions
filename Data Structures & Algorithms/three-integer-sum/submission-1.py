class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort();
        ans = []
        for i in range(n-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            value = nums[i]
            left = i + 1
            right = len(nums) - 1

            
            while left < right:
                curSum = nums[left] + nums[right]
                if curSum + value < 0:
                    left += 1
                elif curSum + value > 0:
                    right -= 1
                else:
                    ans.append([value,nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1

        return ans

        