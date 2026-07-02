class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c1, c2 in zip(word, reversed(word)):
            if (c1, c2) not in node.children:
                node.children[(c1, c2)] = TrieNode()
            node = node.children[(c1, c2)]
            node.count+=1
    
    def count(self, word):
        node = self.root
        for c1, c2 in zip(word, reversed(word)):
            if (c1, c2) not in node.children:
                return 0
            node = node.children[(c1, c2)]
        return node.count
    


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        trie = Trie()
        res = 0
        for word in reversed(words):
            res+=trie.count(word)
            trie.insert(word)
        return res

        