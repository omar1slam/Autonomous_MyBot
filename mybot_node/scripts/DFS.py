import math
from operator import attrgetter
import matplotlib.pyplot as plt
import numpy as np
from timeit import default_timer as time
start = time()
steps = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
borders = [5, 5]
start = time()


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pathx = []
        self.pathy = []

    def __add__(self, other):
        return Node(self.x + other[0], self.y + other[1])

    def __repr__(self):
        return str(self.x) + "," + str(self.y)

    def __eq__(self, other):
        if (self.x == other.x) and (self.y == other.y):
            return True
        else:
            return False


gx = 5
gy = 0
sx = 0
sy = 5

ox = [1,1,1,1,3,3,3,3]
oy = [0,1,2,3,5,4,3,2]

current_node = Node(sx, sy)

queue = [current_node]
discarded = list()

pathx = []
pathy = []


while queue:
    current_node = queue[len(queue)-1]
    queue.pop(len(queue) - 1)
    if (current_node.x, current_node.y) == (gx, gy):
        pathx = [sx] + current_node.pathx
        pathy = [sy] + current_node.pathy
        break
    for i in steps:
        neighbor = current_node + i
        if not((neighbor.x, neighbor.y) in zip(ox, oy)):
            if (neighbor.x, neighbor.y) not in discarded:
                if (0 <= neighbor.x <= borders[0]) and (0 <= neighbor.y <= borders[1]):
                    if neighbor not in queue:
                        neighbor.pathx = current_node.pathx + [neighbor.x]
                        neighbor.pathy = current_node.pathy + [neighbor.y]
                        queue.append(neighbor)

    print(queue)
    discarded.append((current_node.x, current_node.y))

end = time()
print(end-start)
plt.plot(gx, gy, "xb")
plt.plot(sx, sy, "xb")
plt.plot(ox, oy, ".k")
plt.plot(pathx, pathy, "-r")
plt.grid(True)
plt.axis("equal")

plt.show()
