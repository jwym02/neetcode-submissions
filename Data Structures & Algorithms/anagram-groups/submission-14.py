class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        unique_strs = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in unique_strs:
                unique_strs[sorted_word] = [word]
            else:
                unique_strs[sorted_word].append(word)
        
        return list(unique_strs.values())