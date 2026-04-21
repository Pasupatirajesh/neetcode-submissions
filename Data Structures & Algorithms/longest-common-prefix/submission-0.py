class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        prefix = strs[0]
        for string in strs:
            length = 0
            for i in range(len(string)):
                if i < len(prefix) and i < len(string) and string[i] == prefix[i]:
                    length+=1
                else:
                    break
            
            prefix = prefix[:length]
        return prefix

