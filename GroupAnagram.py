class Solution: 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Anagrams = {}
        for word in strs:
            hash_value = [0] * 26
            for char in word:
                hash_value[ord(char) - ord('a')]+=1
            hash_tuple = tuple(hash_value)
            if hash_tuple not in Anagrams:
                Anagrams[hash_tuple] = []
            Anagrams[hash_tuple].append(word)
        return list(Anagrams.values())
