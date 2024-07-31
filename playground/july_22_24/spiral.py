from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        number_of_elements = m * n
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        sol = []
        current_point = (0, 0)
        current_direction = directions[0]

        def switch_direction(current_direction):
            if current_direction == directions[0]: return directions[1]
            if current_direction == directions[1]: return directions[2]
            if current_direction == directions[2]: return directions[3]
            if current_direction == directions[3]: return directions[0]
        
        print(sol)
        while len(sol) < number_of_elements:
            i, j = current_point
            sol.append(matrix[i][j])
            visited.add(current_point)
            print(sol)

            if (i + current_direction[0] >= m
            or i + current_direction[0] < 0
            or j + current_direction[1] >= n
            or j + current_direction[1] < 0
            or (i + current_direction[0], j + current_direction[1]) in visited
            ):
                current_direction = switch_direction(current_direction)
            
            current_point = (i + current_direction[0], j + current_direction[1])
        
        return sol

s = Solution()
s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])