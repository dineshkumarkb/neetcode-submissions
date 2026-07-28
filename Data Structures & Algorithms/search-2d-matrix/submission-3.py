class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # binary search for row
        # binary search for column

        ROWS, COLS = len(matrix), len(matrix[0])

        top = 0 
        bottom = ROWS - 1

        while top <= bottom:
            row = (top + bottom) // 2

            if target > matrix[row][-1]:
                top += 1
            elif target < matrix[row][0]:
                bottom -=1
            else:
                break

        if not(top <= bottom): return False

        row = (top + bottom) // 2

        l, r = 0, COLS - 1

        while l <= r:
            mid = (l + r) // 2
            
            if target == matrix[row][mid]:
                return True
            elif target > matrix[row][mid]:
                l += 1
            elif target < matrix[row][mid]:
                r -= 1

        return False

            




            



        