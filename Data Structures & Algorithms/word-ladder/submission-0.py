class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        transforms = 0

        def buildgenericmap(wordList):
            gm = {}
            for word in wordList:
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i+1:]

                    if pattern not in gm:
                        gm[pattern] = []
                    gm[pattern].append(word)
            return gm
        
        queue = deque()
        visit = set()
        queue.append((beginWord,1))
        visit.add(beginWord)
        g_map = buildgenericmap(wordList)

        while queue:
            word, transforms = queue.popleft()
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]

                for neighbor in g_map.get(pattern, []):
                    if neighbor not in visit:
                        visit.add(neighbor)
                        queue.append((neighbor, transforms+1))

                    if neighbor == endWord:
                        return transforms+1
        return 0
