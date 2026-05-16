# Last updated: 5/16/2026, 12:25:59 PM
class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:

        clips.sort(key = lambda x: (x[0], -x[1]))

        # print("clips=", clips)

        start = 0
        end = 0
        next_end = 0

        count = 0

        for i in range(len(clips)):
            
            if clips[i][1] <= end:
                continue

            elif clips[i][1] > end and clips[i][0] <= end:

                for j in range(i, len(clips)):
                    if clips[j][0] > end:
                        break

                    next_end = max(next_end, clips[j][1])

                count += 1
                end = next_end
                print("start =", start)
                print("end =", end)

            elif clips[i][0] > end:
                
                
                print("start =", start)
                print("end =", end)     
                break           

            if end >= time:
                return count
            

        return -1





































        # clips.sort(key=lambda x: (x[0], -x[1]))

        # count = 0
        # curEnd = 0
        # nextEnd = 0

        # n = len(clips)

        # i = 0

        # while (i < n and clips[i][0] <= curEnd):
            
        #     while (i < n and clips[i][0] <= curEnd):
        #         nextEnd = max(clips[i][1], nextEnd)
        #         i += 1
            
        #     curEnd = nextEnd
        #     count += 1

        #     if (curEnd >= time):
        #         return count
        
        # return -1

