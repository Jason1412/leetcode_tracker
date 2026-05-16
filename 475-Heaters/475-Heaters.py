# Last updated: 5/16/2026, 12:27:53 PM
class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        radius = 0
        i = 0
        for house in houses:
            # find the heaters before and after the house
            while(i < len(heaters)  and house > heaters[i]):
                i += 1
            if i == 0:
                radius = max(radius, heaters[0] - houses[0])
            elif i == len(heaters):
                radius = max(radius, houses[-1] - heaters[-1])

            else:
                radius = max(radius, min(house - heaters[i-1], heaters[i] - house))
        
        return radius 
                