class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    res.append(words[i])
                    break
        return res 
        res = [w1 for i, w1 in enumerate(words) if any(w1 in w2 for j, w2 in enumerate(words) if i != j)]
