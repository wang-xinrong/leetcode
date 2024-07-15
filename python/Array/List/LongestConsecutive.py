from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)
        if len(nums) == 0:
            return 0
        else:
            maxlen = 1

        while (len(myset) > 0):
            e = myset.pop()
            left, right = e-1, e+1
            if (left in myset or right in myset):
                while left in myset:
                    myset.remove(left)
                    left-=1

                while right in myset:
                    myset.remove(right)
                    right+=1

                maxlen = max(maxlen, right-left-1)
        return maxlen
