class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int: 
        queue = []
        time = 0
        for i in range(len(tickets)):
            if i <= k:
                time += min(tickets[i], tickets[k])
            elif i > k:
                time += min(tickets[i], tickets[k]-1)
        return time 


