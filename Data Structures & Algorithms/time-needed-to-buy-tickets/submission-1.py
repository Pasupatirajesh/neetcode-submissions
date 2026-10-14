from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int: 
        queue = deque((tickets[i], i) for i in range(len(tickets)))
        time = 0
        while True:
            remaining_tickets, index = queue.popleft()
            remaining_tickets-=1
            time+=1
            if remaining_tickets > 0:
                queue.append((remaining_tickets, index))
            if index == k:
                if remaining_tickets == 0:
                    return time
            
        


