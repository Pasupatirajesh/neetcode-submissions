class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hash_map = {"2": "abc", 
                   "3": "def",
                   "4": "ghi",
                   "5": "jkl", 
                   "6": "mno",
                   "7": "pqrs",
                   "8": "tuv",
                   "9": "wxyz"}
        res = []
        def backtrack(index, path):
            if digits == "":
                return None
            if len(path) == len(digits):
                res.append("".join(path))
                return
            
            for char in hash_map[digits[index]]:
                path.append(char)
                backtrack(index+1 , path)
                path.pop()
        backtrack(0, [])
        return res 