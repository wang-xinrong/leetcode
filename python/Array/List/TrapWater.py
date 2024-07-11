from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3: return 0
        left, right = 1, len(height)-2
        leftMax, rightMax = height[0], height[-1]
        water=0

        while left<=right:
            if height[left] > leftMax:
                leftMax = height[left]

            if height[right] > rightMax:
                rightMax = height[right]

            if leftMax <= rightMax:
                water+=leftMax-height[left]
                left+=1
            else:
                water+=rightMax-height[right]
                right-=1
        return water
