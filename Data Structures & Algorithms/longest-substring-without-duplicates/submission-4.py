class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        l = 0
        window = set()
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l+=1
                
            
            count = max(count, r-l+1)
            window.add(s[r])
        return count 
