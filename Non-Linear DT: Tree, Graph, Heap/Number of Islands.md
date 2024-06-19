# Number of Islands

테마: Counting

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
- 시간 복잡도: $O(행*열)$
- 공간 복잡도: $O(Queue의 최대 크기)=O(1)$

## DFS를 이용한 방법
```python
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
```
- 시간 복잡도: $O(행*열)$
- 공간 복잡도: $O(행*열)$