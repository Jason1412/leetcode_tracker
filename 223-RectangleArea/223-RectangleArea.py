# Last updated: 5/16/2026, 12:28:52 PM
class Solution:
# Method 2 =========================================================
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        ox1 = max(ax1, bx1)
        oy1 = max(ay1, by1)

        ox2 = min(ax2, bx2)
        oy2 = min(ay2, by2)

        overlap_area = abs((ox2 - ox1) * (oy2 - oy1)) 

        total_area = (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1)
        
        if ox2 - ox1 > 0 and oy2 - oy1 > 0:
            total_area -= overlap_area

        return total_area    


# Method 1 ========================================================
    # def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        

    #     ox1 = max(ax1, bx1)
    #     oy1 = max(ay1, by1)

    #     ox2 = min(ax2, bx2)
    #     oy2 = min(ay2, by2)

    #     # print(ox1, oy1, ox2, oy2)

    #     overlap_area = (ox2 - ox1) * (oy2 - oy1) 

    #     if ox2 - ox1 < 0 or oy2 - oy1 < 0:
    #         overlap_area = - abs(overlap_area)

    #     a_area = (ax2 - ax1) * (ay2 - ay1)
    #     b_area = (bx2 - bx1) * (by2 - by1)

    #     if overlap_area < 0:
    #         total = a_area + b_area
    #     else:
    #         total = a_area + b_area - overlap_area
        
    #     return total