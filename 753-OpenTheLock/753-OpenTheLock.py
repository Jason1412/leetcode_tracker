# Last updated: 5/16/2026, 12:26:59 PM
from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 记录需要跳过的死亡密码
        deads = set(deadends)
        # 记录已经穷举过的密码，防止走回头路
        visited = set()
        q = collections.deque()
        # 从起点开始启动广度优先搜索
        step = 0
        q.append("0000")
        visited.add("0000")

        while q:
            sz = len(q)
            # 将当前队列中的所有节点向周围扩散
            for i in range(sz):
                cur = q.popleft()

                # 判断是否到达终点
                if cur in deads:
                    continue
                if cur == target:
                    return step

                # 将一个节点的未遍历相邻节点加入队列
                for j in range(4):
                    up = self.plusOne(cur,j)
                    if up not in visited:
                        q.append(up)
                        visited.add(up)
                    down = self.minusOne(cur,j)
                    if down not in visited:
                        q.append(down)
                        visited.add(down)
            # 在这里增加步数
            step += 1
        # 如果穷举完都没找到目标密码，那就是找不到了
        return -1

    # 将 s[j] 向上拨动一次
    def plusOne(self, s: str, j: int) -> str:
        ch = list(s)
        if ch[j] == '9':
            ch[j] = '0'
        else:
            ch[j] = chr(ord(ch[j])+1)
        return "".join(ch)

    # 将 s[i] 向下拨动一次
    def minusOne(self, s: str, j: int) -> str:
        ch = list(s)
        if ch[j] == '0':
            ch[j] = '9'
        else:
            ch[j] = chr(ord(ch[j])-1)
        return "".join(ch)

# Method 1 =====================================
    # def openLock(self, deadends: List[str], target: str) -> int:
    #     deads = set(deadends)
    #     queue = deque(['0000'])
    #     visited = set()
    #     visited.add('0000')
    #     depth = 0
    #     while queue:
    #         sz = len(queue)
    #         print('size = ', sz)
    #         for i in range(sz):
    #             q = queue.popleft()
                
    #             if q in deads:
    #                 continue

    #             if q == target:
    #                 return depth

    #             next_lock = self.choices(q, deads, visited)
    #             queue.extend(next_lock)

    #             for lock in next_lock: # This is the key, 
                    
    #                 visited.add(lock)

                
    #         print(visited)
    #         depth += 1
    #     return -1


    # def choices(self, lock_str, deadends, visited):

    #     d = {}
    #     for i, char in enumerate(lock_str):

    #         if int(char) == 0:
    #             d[i] = [9, 1]
    #         elif int(char) == 9:
    #             d[i] = [8, 0]
    #         else:
    #             d[i] = [int(char) - 1, int(char) + 1]

    #     out_str = []

    #     for i, val_list in d.items():
    #         for val in val_list:
    #             tmp = lock_str[:i] + str(val) + lock_str[i+1:]
    #             if tmp in deadends or tmp in visited:
    #                 continue
    #             else:
    #                 out_str.append(tmp)

    #     return out_str
