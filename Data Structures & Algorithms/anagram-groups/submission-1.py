class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       
        map_anagram = {}

        for word in strs:
            key = tuple(sorted(word))
            if key not in map_anagram:
                map_anagram[key] = []
            map_anagram[key].append(word)

        return list(map_anagram.values())


