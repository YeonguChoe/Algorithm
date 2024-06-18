# Number of Islands


## BFS를 이용한 방법
```python
from collections import deque


def numOfIsland(grid):
    row = len(grid)
    column = len(grid[0])
    count = 0

    for y in range(row):
        for x in range(column):
            if grid[y][x] == "1":
                count += 1
                bfs(x, y, grid)
    return count


def bfs(x, y, grid):
    Q = deque([])
    grid[y][x] = "0"
    Q.append([x, y])
    while len(Q) > 0:
        current_cell = Q.popleft()
        current_x = current_cell[0]
        current_y = current_cell[1]
        direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for move in direction:
            neighbor = [current_x + move[0], current_y + move[1]]
            if (
                neighbor[0] in range(len(grid[0]))
                and neighbor[1] in range(len(grid))
                and grid[neighbor[1]][neighbor[0]] == "1"
            ):
                grid[neighbor[1]][neighbor[0]] = "0"
                Q.append(neighbor)
```

