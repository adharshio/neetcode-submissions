#from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+ 1)]

        for i in nums:
            count[i] = count.get(i,0) + 1
        #print(count)
        for i , j in count.items():
            #i = key j = value
            freq[j].append(i)

        
        res = []
        for i in range(len(freq)-1,-1,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
