class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

           
        def get_key(s):
            diffs = []
            for i in range(len(s)-1):
                diff = (ord(s[i+1])-ord(s[i])) % 26
                diffs.append(diff)
            return tuple(diffs)
        
        groups = defaultdict(list)

        for s in strings:
            key = get_key(s)
            groups[key].append(s)
        return list(groups.values())
                