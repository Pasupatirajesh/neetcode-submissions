class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [[matrix[row][col] for row in range(len(matrix))] for col in range(len(matrix[0]))]