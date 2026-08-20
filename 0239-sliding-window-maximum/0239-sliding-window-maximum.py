from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        result = []

        for i in range(len(nums)):
            # Remove indices outside the current window
            while q and q[0] <= i - k:
                q.popleft()

            # Remove smaller elements from the back
            while q and nums[q[-1]] <= nums[i]:
                q.pop()

            q.append(i)

            # Window is complete
            if i >= k - 1:
                result.append(nums[q[0]])

        return result teh