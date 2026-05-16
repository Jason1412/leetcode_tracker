# Last updated: 5/16/2026, 12:25:52 PM
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        diff = [0] * (n+1)

        for booking in bookings:
            i, j, num_seats = booking[0], booking[1], booking[2]
            diff[i-1] += num_seats
            diff[j] -= num_seats

        res = [0] * n
        
        res[0] = diff[0]
        for i in range(1, n):
            res[i] = res[i-1] + diff[i]

        return res