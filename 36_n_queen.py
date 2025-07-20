# Time Complexity: O(N!)
# Space Complexity: O(N^2) – for the board and recursion stack

class Solution:
    def solveNQueens(self, n):
        def backtrack(row, cols, diag1, diag2, board):
            if row == n:
                res.append([''.join(r) for r in board])
                return

            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                board[row][col] = 'Q'
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(row + 1, cols, diag1, diag2, board)

                board[row][col] = '.'
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        res = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        backtrack(0, set(), set(), set(), board)
        return res

# Example
solver = Solution()
solutions = solver.solveNQueens(4)
for solution in solutions:
    for row in solution:
        print(row)
    print()
