class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        pref = strs[0]
        for string in strs:
            length = 0
            for i in range(len(string)):
                if i < len(pref) and pref[i] == string[i]:
                    length+=1
                else:
                    break
            pref = pref[:length]
        return pref 
