from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        row = 0
        col = n - 1

        # matrix length (x)

        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True

            elif matrix[row][col] > target:
                col -= 1

            else:
                row += 1

        return False