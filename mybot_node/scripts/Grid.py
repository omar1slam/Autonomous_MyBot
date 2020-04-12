import numpy as np


height =8
width =8

grid = np.zeros((height,width))

class cell(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.pathx = []
        self.pathy = []


def BFS(grid,start,goal):
    bool1=0
    bool2= 0
    bool3 =0
    bool4 =0
    queue = []
    visited=[]
    i = start[0]
    j = start[1]
    tree = []
    current = [i,j]
    grid[i,j] = 1

    
    while(current != goal):
            
            if i != goal[0] and j != goal[1]:
            
                if i-1 <0:
                    bool1 = 1
                if j-1 <0:
                    bool2 = 1
                if i + 1 > width:
                    bool3 = 1
                if j + 1 > height:
                    bool4 = 1

                if (grid[i,j+1] != 1) & (bool4 != 1):
                    queue.append(i)
                    queue.append(j+1)
                    grid[i][j+1] = 1

                if (grid[i+1,j+1] != 1) & (bool3 != 1) & (bool4 != 1):
                    queue.append(i+1)
                    queue.append(j+1)
                    grid[i][j+1] = 1
                    bool3 = 0
                    bool4 = 0
                
                if (grid[i+1,j] != 1) & (bool3 != 1):
                    queue.append(i+1)
                    queue.append(j)
                    grid[i+1][j] = 1
                    bool3 = 0

                if (grid[i+1,j-1] != 1) & (bool2 != 1) & (bool3 != 1):
                    queue.append(i+1)
                    queue.append(j-1)
                    visited.append(i+1)
                    visited.append(j-1)
                    grid[i+1][j-1] = 1
                    bool2 = 0
                    bool3 = 0

                if (grid[i,j-1] != 1) & (bool2 != 1):
                    queue.append(i)
                    queue.append(j-1)
                    visited.append(i)
                    visited.append(j-1)
                    grid[i][j-1] = 1
                    bool2 = 0
                
                if (grid[i-1,j-1] != 1) & (bool1 != 1) & (bool2 != 1):
                    queue.append(i-1)
                    queue.append(j-1)
                    grid[i-1][j-1] = 1
                    bool1 = 0
                    bool2 = 0


                if (grid[i-1,j+1] != 1) & (bool1 != 1) & (bool4 != 1):
                    queue.append(i-1)
                    queue.append(j+11)
                    grid[i-1][j+1] = 1
                    bool1 = 0
                    bool4 = 0

                if (grid[i-1,j] != 1) & (bool1 != 1):
                    queue.append(i-1)
                    queue.append(j)
                    grid[i-1][j] = 1
                    bool1 = 0
 
            print(queue)
            i = queue[0]
            j = queue[1]
            queue.pop(0)
            queue.pop(0)
            current = [i,j]

    return visited



v = BFS(grid,[0,0],[6,5])


