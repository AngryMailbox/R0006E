import matplotlib.pyplot as plt
import numpy as np
import time

grid_size = (4, 4)
obstacles = [(1, 1), (2, 1), (2, 2)]  # Second coord "inverted" to match the task image on canvas.
start_pos = (0, 0)
target_pos = (3, 3)

def get_neighbors(position):
    x, y = position
    neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    valid_neighbors = [n for n in neighbors if 0 <= n[0] < grid_size[0] and 0 <= n[1] < grid_size[1]]
    valid_neighbors = [n for n in valid_neighbors if n not in obstacles]
    return valid_neighbors

def move_robot(start, target_pos):
    path = [start]
    current_pos = start
    
    while current_pos != target_pos:
        neighbours = get_neighbors(current_pos)
        next_pos = min(neighbours, key=lambda pos: (pos[0] - target_pos[0])**2 + (pos[1] - target_pos[1])**2)
        path.append(next_pos)
        current_pos = next_pos
        plot_grid(path, start, target_pos)
    return path

def plot_grid(path, start, goal):
    grid = np.ones(grid_size) * 0.5
    for obs in obstacles:
        grid[obs] = 0.2

    plt.imshow(grid, cmap='gray', origin='upper')
    
    # startpos
    plt.fill([start[1]-0.5, start[1]+0.5, start[1]+0.5, start[1]-0.5], 
             [start[0]-0.5, start[0]-0.5, start[0]+0.5, start[0]+0.5], 
             color='blue', label='Start')

    # goalpos
    plt.fill([goal[1]-0.5, goal[1]+0.5, goal[1]+0.5, goal[1]-0.5], 
             [goal[0]-0.5, goal[0]-0.5, goal[0]+0.5, goal[0]+0.5], 
             color='green', label='Goal')

    for obs in obstacles:
        plt.fill([obs[1]-0.5, obs[1]+0.5, obs[1]+0.5, obs[1]-0.5], 
                 [obs[0]-0.5, obs[0]-0.5, obs[0]+0.5, obs[0]+0.5], 
                 color='black', label='Obstacle' if obs == obstacles[0] else "")

    for step in path:
        plt.scatter(step[1], step[0], color='cyan', s=100)

    plt.xticks(range(4))
    plt.yticks(range(4))
    plt.grid(True)
    plt.gca().invert_yaxis()
    plt.pause(0.5)
    plt.clf()

plt.ion()
path = move_robot(start_pos, target_pos)
plt.ioff()
time.sleep(9999)
