from typing import List
from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = defaultdict(list)
        for i in range(len(nums)):
            dict[nums[i]].append(i)
        
        for i in nums:
            j = target - i
            if i == j and len(dict[i]) >= 2:
                return dict[i]
            elif dict[j] and i != j:
                return [dict[i][0], dict[j][0]]

    def twoSumFaster(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        l = len(nums)
        for i in range(l):
            if target - nums[i] in dict:
                return [dict[target - nums[i]], i]
            dict[nums[i]] = i
        return []