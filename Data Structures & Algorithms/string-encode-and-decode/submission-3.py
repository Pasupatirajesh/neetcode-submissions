class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for string in strs:
            encoded+= str(len(string))+ '#' + string
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            initial_length = i
            while s[i] != '#':
                i+=1
            length = int(s[initial_length: i])
            i+=1
            substring = s[i: i+length]
            decoded.append(substring)
            i+=length
        return decoded
            
