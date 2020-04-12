#! /usr/bin/env python
import math
from operator import attrgetter
import matplotlib.pyplot as plt
import cv2
from std_msgs.msg import String, Float32MultiArray
import rospy
import numpy as np

steps = [(0, -1), (1, 1), (1, 0), (1, -1), (0, 1), (-1, -1), (1, 0), (-1, -1)]

rospy.init_node('Planner',anonymous=True)
pub= rospy.Publisher('path',Float32MultiArray,queue_size=10)
msg = Float32MultiArray()
#img = cv2.imread("map.jpeg")[:, :, 0]

#img = cv2.resize(img, (500, 350), interpolation=cv2.INTER_AREA)

#borders = img.shape


borders = [5, 5]


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


gx = int(raw_input("Please enter x-coordinate:  "))
gy = int(raw_input("Please enter y-coordinate:  "))
print(gx,gy)

sx = 0
sy = 0  

"""
ox = list()
oy = list()


for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img[i, j] > 100:
            ox.append(float(j))
            oy.append(float(i))
"""
ox = []
oy = []


current_node = Node(sx, sy)

queue = [current_node]
discarded = list()

pathx = []
pathy = []

while not len(queue) == 0:
    current_node = queue[0]
    if (current_node.x, current_node.y) == (gx, gy):
        pathx = [sx] + current_node.pathx
        pathy = [sy] + current_node.pathy
        break
    for i in steps:
        neighbor = current_node + i
        if not((neighbor.x, neighbor.y) in zip(ox, oy)):
            if (neighbor.x, neighbor.y) not in discarded:
                if (0 <= neighbor.x <= borders[0]) and (0 <= neighbor.y <= borders[1]):
                    for node in range(len(queue)):
                        if (queue[node].x, queue[node].y) == (neighbor.x, neighbor.y):
                            break
                        if node == len(queue) - 1:
                            neighbor.pathx = current_node.pathx + [neighbor.x]
                            neighbor.pathy = current_node.pathy + [neighbor.y]
                            queue.append(neighbor)

    #print(queue)
    discarded.append((current_node.x, current_node.y))
    del queue[0]

msg.data = pathx+pathy
pub.publish(msg)

plt.plot(gx, gy, "xb")
plt.plot(sx, sy, "xb")
plt.plot(ox, oy, ".k")
plt.plot(pathx, pathy, "-r")
plt.grid(True)
plt.axis("equal")

plt.show()





