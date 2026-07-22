class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = Counter(s)
        odd_count = 0
        for char, freq in count.items():
            if freq %2 != 0:
                odd_count+=1
        
        if odd_count <=1:
            return True
        return False 
            
