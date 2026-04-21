class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True 
        

    def search(self, word: str) -> bool:
        curr = self.root
        def dfs(node, index):
            if index == len(word):
                return node.word
            char = word[index]
            if char == ".":
                for child in node.children.values():
                    if dfs(child, index+1):
                        return True
                return False
            else:
                if char not in node.children:
                    return False 
                return dfs(node.children[char], index+1)
            
        return dfs(curr, 0) 

        
