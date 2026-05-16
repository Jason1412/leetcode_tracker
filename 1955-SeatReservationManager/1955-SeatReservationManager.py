# Last updated: 5/16/2026, 12:25:27 PM
class SeatManager:

    def __init__(self, n: int):
        self.seats = list(range(1, n+1, 1))
        

    def reserve(self) -> int:
        return self.seats.pop(0)

    def unreserve(self, seatNumber: int) -> None:
        ind = 0
        for i in range(len(self.seats)):
            if self.seats[i] > seatNumber:
                ind = i
                break


        self.seats.insert(ind, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)