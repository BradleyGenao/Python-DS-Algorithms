def remove_ones(grid):
    rows = len(grid)
    row_orig = grid[0]
    row_flipped = [1-x for x in grid[0]]
    
    for row in range(1, rows):
        if grid[row] != row_orig and grid[row] != row_flipped:
            return False
    return True

grid1 = [[0,1,0],[1,0,1],[0,1,0]]
grid2 = [[1,1,0],[0,0,0],[0,0,0]]
print("Expected: True Actual: {}".format(remove_ones(grid1)))
print("Expected: False Actual: {}".format(remove_ones(grid2)))
