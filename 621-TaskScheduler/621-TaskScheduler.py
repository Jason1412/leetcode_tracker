# Last updated: 5/16/2026, 12:27:22 PM
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        print(freq)
        freq.sort()

        max_freq = freq[25] - 1

        idle_slots = (max_freq) * n

        print("idle_slots=", idle_slots)

        for i in range(24, -1, -1):
            idle_slots -= min(max_freq, freq[i])

        print("After idle_slots=", idle_slots)

        return idle_slots + len(tasks) if idle_slots > 0 else len(tasks)