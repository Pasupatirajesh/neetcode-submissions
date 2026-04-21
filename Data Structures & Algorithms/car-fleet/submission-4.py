class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        posspeed = []

        for p, s in zip(position, speed):
            posspeed.append([p,s])
        
        for p, s in sorted(posspeed)[::-1]:
            rank = (target - p) / s

            stack.append(rank)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
            
        return len(stack)
