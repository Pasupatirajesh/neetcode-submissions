class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        balance = defaultdict(int)
        
        # Min and max tracking tells us exactly where to start and stop scanning
        min_pos = float('inf')
        max_pos = float('-inf')
        
        for seat in seats:
            balance[seat] += 1
            min_pos = min(min_pos, seat)
            max_pos = max(max_pos, seat)
            
        for stu in students:
            balance[stu] -= 1
            min_pos = min(min_pos, stu)
            max_pos = max(max_pos, stu)
            
        moves = 0
        current_balance = 0
        
        # Scan across the number line from the lowest active point to the highest
        for pos in range(min_pos, max_pos + 1):
            current_balance += balance[pos]
            # The absolute value of the running balance represents 
            # the number of "unmatched" entities passing through this position
            moves += abs(current_balance)
        return moves
        