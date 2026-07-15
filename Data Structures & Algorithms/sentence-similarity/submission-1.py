class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        pairs = defaultdict(set)
        for w1, w2 in similarPairs:
            pairs[w1].add(w2)
            pairs[w2].add(w1)

        for i  in range(len(sentence1)):    
            if sentence1[i] == sentence2[i]:
                continue
            elif sentence2[i] in pairs[sentence1[i]]:
                continue
            return False
        return True

    
