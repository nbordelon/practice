# https://leetcode.com/problems/last-stone-weight/

# You are given an array of integers stones where stones[i] is the weight of the ith stone.

# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.

# Return the weight of the last remaining stone. If there are no stones left, return 0.

import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        
        # Negative vals to turn min heap -> max heap
        for x in range(len(stones)):
            stones[x] *= -1
        
        # Heapify negative values (max heap)
        heapq.heapify(stones)
 
        while(len(stones)>1):
            first = abs(heapq.heappop(stones))
            second = abs(heapq.heappop(stones))

            if (second < first):
                heapq.heappush(stones, (second-first))

        if len(stones) == 0:
            stones.append(0)

        return abs(stones[0])

if __name__ == '__main__':
    # Please separate inputs with an empty space. (1 2 3)
    usrInpt = list(map(int,(input("Enter your test case: ").strip().split())))
    print(Solution().lastStoneWeight(usrInpt))