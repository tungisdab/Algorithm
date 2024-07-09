grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]
n = len(grid)
for i in range(n):
    for j in range(n):
        if j == i:
            if grid[i][j] == 0:
                # return False
                print(1)
        if j == n - 1 - i:
            if grid[i][j] == 0:
                # return False
                print(2)
        else:
            if grid[i][j] != 0:
                print(i, j)
                # return False
                print(3)
        # return True