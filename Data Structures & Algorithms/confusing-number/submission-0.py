class Solution:
    def confusingNumber(self, n: int) -> bool:
        for digit in str(n):
            if digit in '23457':
                return False
        
        mapping = {'0': '0', '1':'1', '6':'9', '8':'8', '9':'6'}
        rotated = ''.join(mapping[d] for d in str(n))

        return rotated[::-1] != str(n)