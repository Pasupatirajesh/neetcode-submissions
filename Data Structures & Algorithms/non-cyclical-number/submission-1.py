class Solution:
    def isHappy(self, n: int) -> bool:
        hash_set = set()

        def helper(num):
            return sum(int(digit) ** 2 for digit in str(abs(num)))


        slow = n
        fast = helper(n)

        while slow != fast:
            slow = helper(slow)
            fast = helper(helper(fast))
        
        if fast == 1:
            return True
        else:
            return False