class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        rev_num = 0
        original = x
        while x != 0:
            digit = x % 10
            rev_num = (rev_num * 10) +digit
            x//=10
        return original == rev_num
