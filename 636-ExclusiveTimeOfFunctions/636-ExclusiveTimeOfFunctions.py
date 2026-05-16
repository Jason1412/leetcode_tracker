# Last updated: 5/16/2026, 12:27:19 PM
from collections import OrderedDict

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        stack = []
        func_time = OrderedDict()
        prev_ts = 0
        prev_flag = None

        for i in range(len(logs)):
            fid, flag, ts = logs[i].split(':')
            ts = int(ts)

            if not stack:
                stack.append((fid, flag, ts))
                prev_ts = ts
                prev_flag = flag
                continue
            
            if flag == 'start':
                prev_fid, _, _ = stack[-1]
                
                if prev_flag == 'start':
                    gap = ts - prev_ts
                elif prev_flag == 'end':
                    gap = ts - prev_ts - 1

                if prev_fid not in func_time:
                    func_time[prev_fid] = gap
                else:
                    func_time[prev_fid] += gap
                
                stack.append((fid, flag, ts))


            if flag == 'end':
                prev_fid, _, _ = stack.pop()

                if prev_flag == 'start':
                    gap = ts - prev_ts + 1
                elif prev_flag == 'end':
                    gap = ts - prev_ts

                if prev_fid not in func_time:
                    func_time[prev_fid] = gap
                else:
                    func_time[prev_fid] += gap
            
            prev_ts = ts
            prev_flag = flag

        n_func = len(func_time.keys())


        return [func_time[str(i)] for i in range(n_func)] 