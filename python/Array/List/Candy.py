class Solution:
    def candy(self, ratings: List[int]) -> int:
        l = len(ratings)
        result = [1] * l

        for i in range(1, l):
            if ratings[i] > ratings[i - 1]:
                result[i] = result[i - 1] + 1
        
        for j in range(l - 2, -1, -1):
            if ratings[j] > ratings[j+1]:
                result[j] = max(result[j], result[j + 1] + 1)
        
        return sum(result)
