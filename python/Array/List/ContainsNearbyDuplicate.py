from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict = {}

        for i, n in enumerate(nums):
            if (n in dict) and (i - dict[n] <= k):
                return True
            dict[n] = i

        return False
        