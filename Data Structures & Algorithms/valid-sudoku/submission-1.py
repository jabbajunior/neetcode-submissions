class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = defaultdict(list), defaultdict(list)

        for r in range(9):
            for c in range(9):
                rows[r].append(board[r][c])
                cols[c].append(board[r][c])

        values = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}

        # Ensures each row has no duplicates
        for r in rows:
            # Remove each row value from set of 1-9 and if it throws an error, means there is a duplicate!
            copy = set(values)
            for num in rows[r]:
                # Skip empty cells
                if num != ".":
                    try:
                        copy.remove(num)
                    except:
                        return False

        # Ensures each column has no duplicates
        for c in cols:
            copy = set(values)
            for num in cols[c]:
                if num != ".":
                    try:
                        copy.remove(num)
                    except:
                        return False

        # Sub grids (0 - 2, 3 - 5, 6 - 8)

        # Need to cover all 9 subgrids
        # Have the logic, just need the actual indexing to work out

        # Loop through entire matrix, but maintain a list of 9 sets containnig the sets for each sub-grid
        subgrid_values = [set(values) for _ in range(9)]

        for r in range(9):
            for c in range(9):

                if rows[r][c] != ".":
                    try:
                        grid_num = r // 3 * 3 + c // 3
                        subgrid_values[grid_num].remove(rows[r][c])
                    except:
                        return False

        # Sub Grid 1 (0 - 2)
        copy = set(values)
        for i in range(3):
            for j in range(3):
                if rows[i][j] != ".":
                    try:
                        copy.remove(rows[i][j])
                    except:
                        return False

        return True
