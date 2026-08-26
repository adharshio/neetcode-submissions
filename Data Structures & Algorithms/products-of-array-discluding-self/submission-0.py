class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeroCount = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                product *= nums[i]
            else:
                zeroCount += 1

        output = [0] * len(nums)
        '''
        now i have product without zero and list of indexes where there is zero

        now i have to check wheather any of the nums[i] is not in the zeroIdx 
        if so then it output becomes non zero product , otherwise it would just become zero 
        '''
        for i in range(len(nums)):
            if zeroCount == 0:
                output[i] = product // nums[i]
            elif zeroCount == 1 and nums[i] == 0:
                output[i] = product
            else:
                output[i] = 0
        
        return output