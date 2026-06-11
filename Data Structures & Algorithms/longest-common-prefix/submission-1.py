class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        for i in range(len(strs[0])):        # loop through positions of first word
            
            for word in strs:        # loop through every other word
                
                if i == len(word) or strs[0][i] != word[i]:   # two stop conditions
                    return strs[0][:i]
        
        return strs[0]