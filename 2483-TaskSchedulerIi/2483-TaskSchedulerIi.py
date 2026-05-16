# Last updated: 5/16/2026, 12:25:20 PM
class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        
        dd = {}
        count = 0

        for i in range(len(tasks)):
            if tasks[i] not in dd:
                dd[tasks[i]] = count
                count += 1
            else:
                if count - dd[tasks[i]] - 1 < space:
                    count += space - (count - dd[tasks[i]] - 1)
                    dd[tasks[i]] = count
                    count += 1
                else:
                    dd[tasks[i]] = count
                    count += 1
            # print('dd=', dd)
        return count

                
