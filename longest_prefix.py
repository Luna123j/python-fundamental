
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ""
        temp = ""
        l = len(min(strs,key=len))
        
        if ( len(strs) < 1):
            return result
        
        
        for i in range(0,l):
            temp = strs[0][i]
            for word in strs:
                if word[i] != temp:
                    result = word[0:i]
                    return result
           
        result = min(strs,key=len)
        
        return result