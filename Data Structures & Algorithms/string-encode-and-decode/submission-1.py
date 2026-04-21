class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for string in strs:
            encoded+= str(len(string))+ '#'+string
        return encoded
        
    def decode(self, s: str) -> List[str]:
        decode = []
        i = 0
        while i < len(s):
            N = i
            while s[i] != '#':
                i+=1
            length = int(s[N: i])
            i+=1
            
            decode.append(s[i: i+length])
            i+=length
        return decode


        
