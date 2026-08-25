class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            word_length = len(word)
            res += str(word_length) + "#" + word

        return res

    def decode(self, s: str) -> List[str]:

        result = []

        i = 0

        while i < len(s):
            j  = i
            while s[j] != "#":
                j += 1
            word_length = int(s[i:j])
            st_idx = j + 1
            end_idx = st_idx + word_length
            result.append(s[st_idx:end_idx])
            
            i = end_idx
        
        return result 