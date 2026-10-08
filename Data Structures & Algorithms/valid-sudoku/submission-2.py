class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)]                # Maintain a set of 9 independent column sets
        subgrid_values = [set() for _ in range(9)]      # Maintain a set of 9 independent subgrid sets

        for r in range(9):
            row = set()
            for c in range(9):
                cur = board[r][c]

                # Do not check empty values
                if cur != '.':

                    # If already seen this value in this row, not valid
                    if cur in row:
                        return False
                    row.add(cur)    # Otherwise add it to row

                    # if already seen in this column, not valid
                    if cur in cols[c]:
                        return False
                    cols[c].add(cur) # Otherwise add it to column

                    # Calculate which sub grid we are in
                    grid_num = r // 3 * 3 + c // 3


                    if cur in subgrid_values[grid_num]:
                        return False
                    subgrid_values[grid_num].add(cur)

        return True