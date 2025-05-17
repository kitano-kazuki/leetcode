directions = [(-1,0), (1,0), (0,1), (0,-1)]
n = 3
m = 4

def is_possible(day, plan):
    grid = [[0] * m for i in range(n)]
    for p in plan[:day + 1]:
        x, y = p
        grid[x][y] = 1
    queue = []
    for i in range(n):
        if grid[i][0] == 0:
            queue.append((i,0))
    while queue:
        x, y = queue.pop(0)
        grid[x][y] = 1
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if ny == m - 1:
                    return True
                if grid[nx][ny] != 1:
                    queue.append((nx,ny))
    return False



def search_days(left, right, plan):
    mid = (left + right ) // 2
    if mid == left:
        if(is_possible(mid, plan)):
            print(f"Possible at {mid}")
            return left
        else:
            print(f"Not Possible at {mid}")
            return left - 1
    if (is_possible(mid, plan)):
        print(f"Possible at {mid}")
        return search_days(mid + 1 , right, plan)
    else:
        print(f"Not Possible at {mid}")
        return search_days(left, mid - 1, plan)


def day_to_stop(n, m, plan, last_day):
    left = 0
    right = last_day
    return search_days(left, right ,plan)

plan = [(0,0),(1,0),(1,1), (1,2), (1,3)]
last_day = len(plan) - 1
day = day_to_stop(n, m ,plan, last_day) + 1
print(day)
