class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_map = {}
        word_map = {}
        s_list = list(s.split(" "))
        if len(pattern) != len(s_list):
            return False
        for c, w in zip(pattern, s_list):
            if c in pattern_map and pattern_map[c] != w:
                return False
            if w in word_map and word_map[w] != c:
                return False
            
            pattern_map[c] = w
            word_map[w] = c
        return True 

            