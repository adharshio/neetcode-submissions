from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        sorted_freq = {k:v for k,v in sorted(freq.items(),key=lambda item:item[1] ,reverse=True)}
        result = []
        counter = 0

        for key in sorted_freq:
            if counter < k:
                result.append(key)
                counter += 1
            else:
                break
        return result
