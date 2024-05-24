""" 
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        
        min_word_len = len(min(strs, key=len))
        if min_word_len == 0:
            return common_prefix

        for i in range(min_word_len):
            common_char = strs[0][i]
            consists = True
            for word in strs[1:]:
                if word[i] != common_char:
                    consists = False
                    break
            if consists:
                common_prefix += common_char
            else:
                break
        
        return common_prefix
