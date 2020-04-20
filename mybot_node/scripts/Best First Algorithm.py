import math
from operator import attrgetter
import matplotlib.pyplot as plt
import numpy as np
from timeit import default_timer as time
start = time()
steps = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
borders = [5, 5]
start = time()

gx = 5
gy = 5


class Node:

    global gx , gy

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pathx = []
        self.pathy = []
        self.dist = np.sqrt(((gx-self.x)**2 + (gy-self.y)**2))

    def __add__(self, other):
        return Node(self.x + other[0], self.y + other[1])

    def __repr__(self):
        return str(self.x) + "," + str(self.y)

    def __eq__(self, other):
        if (self.x == other.x) and (self.y == other.y):
            return True
        else:
            return False


sx = 0
sy = 5

""" Coordinates of obstacles"""
ox = [1,1,1,1,3,3,3]
oy = [0,1,2,3,5,4,3]

current_node = Node(sx, sy)

queue = [current_node]
discarded = list()

pathx = []
pathy = []
bool = 1


while 1:

    if (current_node.x, current_node.y) == (gx, gy):
        pathx = [sx] + current_node.pathx
        pathy = [sy] + current_node.pathy
        break

    discarded.append((current_node.x, current_node.y))
    sorted_queue = sorted(queue, key=attrgetter('dist'))
    sorted_queue[0].pathx = current_node.pathx + [sorted_queue[0].x]
    sorted_queue[0].pathy = current_node.pathy + [sorted_queue[0].y]
    current_node = sorted_queue[0]
    queue = []
    #sorted_queue.clear()

    for i in steps:
        neighbor = current_node + i
        if not((neighbor.x, neighbor.y) in zip(ox, oy)):
            if (neighbor.x, neighbor.y) not in discarded:
                if (0 <= neighbor.x <= borders[0]) and (0 <= neighbor.y <= borders[1]):
                    queue.append(neighbor)

    print(queue)


end = time()
print(end-start)
plt.plot(gx, gy, "xb")
plt.plot(sx, sy, "xb")
plt.plot(ox, oy, ".k")
plt.plot(pathx, pathy, "-r")
plt.grid(True)
plt.axis("equal")

plt.show()
