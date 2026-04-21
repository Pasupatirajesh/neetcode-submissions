class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash_map = {}
    
        res = []
        
        for i in range(len(s)):
            hash_map[s[i]] = i
        max_reach = 0
        last_split = -1
        for i in range(len(s)):
            max_reach = max(max_reach, hash_map[s[i]])
            if i == max_reach:
                res.append(i - last_split)
                last_split = i
        return res
