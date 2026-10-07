class Solution:
    def isHappy(self, n: int) -> bool:
        hash_set = set()

        def helper(num):
            return sum(int(digit) ** 2 for digit in str(abs(num)))


        while n != 1 and n not in hash_set:
            hash_set.add(n)
            n = helper(n)
            
        return n == 1