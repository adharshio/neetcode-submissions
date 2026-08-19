class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        n = len(nums)
        """
            store as {value : index}
            loop through each value 
            find the need value
            
        """
        for i in range(n):
            need = target - nums[i]
            if need in seen:
                return [seen[need],i]
            else:
                seen[nums[i]] = i

        return -1

        