from typing import List


class Solution:

    def getCandidates(self, row, col, board):
        base = set(('1', '2', '3', '4', '5', '6', '7', '8', '9'))
        found = set()

        for i in range(9):
            # scan row
            found.add(board[row][i])
            # scan col
            found.add(board[i][col])

        # scan sector
        rs = int(row / 3) * 3
        cs = int(col / 3) * 3
        for r in range(rs, rs + 3):
            for c in range(cs, cs + 3):
                found.add(board[r][c])

        return list(base - found)

    def solve(self, board):

        # minimum candidate cell
        target_cell = None
        target_candidates = None

        # 1. find the cell which has least candidates
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":

                    candidates = self.getCandidates(i, j, board)
                    candi_count = len(candidates)

                    if candi_count == 0:
                        return False

                    if candi_count == 1:
                        target_cell = (i, j)
                        target_candidates = candidates
                        break

                    if target_cell is None:
                        target_cell = (i, j)
                        target_candidates = candidates
                    else:
                        if len(target_candidates) > len(candidates):
                            target_cell = (i, j)
                            target_candidates = candidates

        if target_cell is None:
            return True  # all cells filled
        if target_candidates is None:
            return False  # empty cell has no candidate

        # 2. fill the cell while try out all candidates recursively
        for candidate in target_candidates:
            board[target_cell[0]][target_cell[1]] = candidate
            if self.solve(board):
                return True
            else:
                board[target_cell[0]][target_cell[1]] = "."

        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)


