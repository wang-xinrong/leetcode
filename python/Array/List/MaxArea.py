from typing import List

class Solution:
    # solution similar to TrapWater
    def maxArea(self, height: List[int]) -> int:
        if (len(height) == 2): return min(height[0], height[1])
        i, j = 1, len(height) - 1
        leftmax, rightmax = height[0], height[-1]
        leftmax_index, rightmax_index = 0, len(height) - 1
        maxArea = (len(height) - 1) * min(leftmax, rightmax)

        while (i < j):
            if height[i] > leftmax:
                leftmax = height[i]
                leftmax_index = i
            
            if height[j] > rightmax:
                rightmax = height[j]
                rightmax_index = j

            if leftmax < rightmax:
                maxArea = max(maxArea, (rightmax_index - leftmax_index) * leftmax)
                i+=1
            else:
                maxArea = max(maxArea, (rightmax_index - leftmax_index) * rightmax)
                j-=1
        return maxArea
    
    def maxAreaWithOptimisation(self, height: List[int]) -> int:
        i, j, maxArea = 0, len(height) - 1, 0
        while (i < j):
            minHeight = min(height[i], height[j])
            maxArea = max(maxArea, minHeight * (j - i))
            if height[i] < height[j]:
                i += 1
                while height[i] < minHeight:
                    i += 1
            else:
                j -= 1
                while height[j] < minHeight:
                    j -= 1

        return maxArea

        