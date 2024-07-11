from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        n, z, p = [], [], []
        for i in nums:
            if i < 0:
                n.append(i)
            elif i == 0:
                z.append(i)
            else:
                p.append(i)
        
        nset, pset = set(n), set(p)
        if len(z) > 0:
            for i in nset:
                if -1*i in pset:
                    result.add((i, 0, -1*i))

            if len(z) >= 3:
                result.add((0, 0, 0))
            
        for i in range(len(n) - 1):
            for j in range(i + 1, len(n)):
                target = -1*n[i] - n[j]
                if target in pset:
                    result.add(tuple(sorted([n[i], n[j], target])))
            
        for i in range(len(p) - 1):
            for j in range(i + 1, len(p)):
                target = -1*p[i] - p[j]
                if target in nset:
                    result.add(tuple(sorted([target, p[i], p[j]])))

        return result
