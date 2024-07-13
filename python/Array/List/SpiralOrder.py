from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def oneRound(matrix: List[List[int]]) -> List[int]:
            if (len(matrix) == 0):
                return []
            elif (len(matrix) == 1):
                return matrix[0]
            elif len(matrix[0]) == 1:
                res = []
                for i in matrix:
                    res+=i
                return res
            upper_row = matrix[0]
            lower_row = matrix[-1][::-1]
            right_side = []
            left_side = []
            for j in range(1, len(matrix) - 1):
                right_side.append(matrix[j][len(matrix[0]) - 1])
                left_side.append(matrix[len(matrix) - 1 - j][0])

            return upper_row + right_side + lower_row + left_side
        if len(matrix) > 2 and len(matrix[0]) > 2:
            return oneRound(matrix) + self.spiralOrder([row[1:-1] for row in matrix[1:-1]])
        else:
            return oneRound(matrix)