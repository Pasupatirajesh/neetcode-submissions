class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        max_index = max(max(seats), max(students)) + 1
        count_seats = [0] * max_index
        count_stu = [0] * max_index

        i, j = 0, 0
        res = 0
        remain = len(seats)
        for seat in seats:
            count_seats[seat]+=1
        for stu in students:
            count_stu[stu] += 1
        while remain:
            if count_seats[i] == 0:
                i+=1
            if count_stu[j] == 0:
                j+=1
            if count_seats[i] and count_stu[j]:
                res+= abs(i-j)
                count_seats[i] -=1
                count_stu[j]-=1
                remain -=1
        return res 
        