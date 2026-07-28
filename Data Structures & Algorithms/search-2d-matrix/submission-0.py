class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Iterate through every row
        # for every row do a binary search for value


        for i in range(len(matrix)):

            if target > matrix[i][-1]:
                continue

            l = 0
            r = len(matrix[i])

            while l < r:

                mid = (l + r) // 2
                pivot = matrix[i][mid]

                if pivot == target:
                    return True
                elif pivot < target:
                    l += 1
                elif pivot > target:
                    r -= 1

        return False




            



        