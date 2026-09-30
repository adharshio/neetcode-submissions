class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        for i in nums:
            count[i] = count.get(i,0) + 1
        print(count)
        for key,values in count.items():
            if values == 1:
                return key