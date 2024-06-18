def numOfIsland(grid):
    count = 0
    row = len(grid)
    column = len(grid[0])

    for y in range(column):
        for x in range(row):
            if grid[y][x] == "1":
                count += 1
                dfs(x, y, grid)
    return count


def dfs(current_x, current_y, grid):
    row = len(grid)
    column = len(grid[0])
    if (
        current_x not in range(column)
        or current_y not in range(row)
        or grid[current_y][current_x] == "0"
    ):
        return
    else:
        grid[current_y][current_x] = "0"
        dfs(current_x + 1, current_y, grid)
        dfs(current_x, current_y + 1, grid)
        dfs(current_x - 1, current_y, grid)
        dfs(current_x, current_y - 1, grid)


input = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]

print(numOfIsland(input))
