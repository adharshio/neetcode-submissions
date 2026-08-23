class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        anagrams = defaultdict(list)
        for words in strs:
            count = [0] * 26
            for chars in words:
                count[ord(chars) - ord('a')] += 1
            answer = tuple(count)
            anagrams[answer].append(words)

        return list(anagrams.values())

            
            