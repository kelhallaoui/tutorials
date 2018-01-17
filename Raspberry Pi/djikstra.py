import numpy as np
from sense_hat import SenseHat
import time

class Environment(object):
    
    def __init__(self, map_size, wall_proportion):
        self.map_size = map_size
        self.wall_prop = int(wall_proportion * map_size**2) # Compute the number of tiles which will be filled by a box
        
        self.env = np.zeros((map_size, map_size))
        
        self.target = None
        
        self.setWalls()
        self.setTarget()
        
    def setWalls(self):
        temp = self.env.reshape((self.map_size**2, 1))
        x = np.random.permutation(self.map_size**2)
        temp[x[0:self.wall_prop]]= 1
        self.env = temp.reshape((self.map_size, self.map_size))
        
    def setTarget(self):
        x, y = np.random.randint(0, self.map_size), np.random.randint(0, self.map_size)
        while(self.env[x, y] == 1):
            x, y = np.random.randint(0, self.map_size), np.random.randint(0, self.map_size)
        self.target = (x, y)
        
    def getEnvironment(self):
        return self.env
    
    def getTarget(self):
        return self.target
    
    def getDists(self):
        board = self.env
        target = self.target
        
        distances = np.full(board.shape, np.inf)
        distances[target] = 0
    
        end = 0
        dist = 0
        curr_node = target
        while True:
            # Get the list of indices that are equal to the current distance
            ixs = np.where(distances == dist)
            dist = dist + 1
        
            # If distance is not in the matrix then we are done. We have reached the maximum 
            if len(ixs[0]) == 0: break
        
            # For each index in the matrix
            for i in range(0, len(ixs[0])):
                curr_node = (ixs[0][i], ixs[1][i])
                # Define the search area as top, bottom, left and right
                for i in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                    # Make sure the board is within the bounds. Need to catch the -1 because it doesnt throw an error
                    if curr_node[0]+i[0] >= 0 and curr_node[1]+i[1] >= 0:
                        try:
                            ix = (curr_node[0]+i[0], curr_node[1]+i[1])
                            # If the board space is available and has not yet been attributed a distance
                            if not board[ix] == 1 and distances[ix] == np.inf: distances[ix] = dist
                        except IndexError:
                            pass
        self.distances = distances
        return distances
    
    def plotEnvironment(self):
        env = self.env
        env[self.target[0], self.target[1]] = 0.5
        plt.imshow(self.env, cmap = 'gray_r')
        plt.show()


def getDistDijkstra(board, init_node, target, verbose = 1):

    values = np.full(board.shape, np.inf)
    unvisited = np.ones(board.shape, dtype=bool)   

    values[init_node] = 0
    unvisited[init_node] = False
    
    if verbose == 1:
        print(values)
        print('Unvisited: \n' + str(unvisited))
        print('-----------------------------------')
        
    end = 0
    curr_node = init_node
    
    while end == 0:
        if verbose == 1: print('Current node: ' + str(curr_node))
        
        for i in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            # Make sure the board is within the bounds. Need to catch the -1 because it doesnt throw an error
            if curr_node[0]+i[0] >= 0 and curr_node[1]+i[1] >= 0:
                try:
                    ix = (curr_node[0]+i[0], curr_node[1]+i[1])
                    if not board[ix] == 1:
                        if values[ix] > values[curr_node] + 1: 
                            values[ix] = values[curr_node] + 1
                except IndexError:
                    if verbose == 1:
                        print('ERROR')
                        pass
        
        unvisited[curr_node] = False   
        
        if verbose == 1:
            print('Unvisited: \n' + str(unvisited))
            print('Values: \n' + str(values))
        
        if not unvisited[target]: 
            if verbose == 1: print('Target found')
            end = 1
        elif np.min(values[unvisited]) == np.inf:
            if verbose == 1: print('Nothing else')
            end = 1
        else:
            minim = np.inf
            ix = [0, 0]
            for i in range(0, size):
                for j in range(0, size):
                    if unvisited[i, j] == True:
                        if values[i, j] < minim:
                            minim = values[i, j]
                            ix = (i, j)
            curr_node = ix
            if verbose == 1:
                print('Update node to: ' + str(curr_node))
        #print('-----------------------------------')
    
    return values[target]

size = 8

sense = SenseHat()
sense.set_rotation(90)
sense.clear(0, 0, 255)

env = Environment(size, 1/7)
board = env.getEnvironment()

print(board)

target = env.getTarget()
board[target] = 0.5
print('Target: ' + str(target))

print('Board')
print(board)

distances = np.zeros((size, size))
for i in range(0, size):
    for j in range(0, size):
        if not board[i,j] == 1:
            distances[i,j] = getDistDijkstra(board, (i,j), target, 0)
        else:
            distances[i, j] = -1
            
print(distances)

print(np.nanmax(distances))
maximum = np.nanmax(distances[distances != np.inf])
for i in range(0, size):
    for j in range(0, size):
        if distances[i,j] == -1:
            sense.set_pixel(i, j, 255, 255, 255)
        elif distances[i,j] == 0:
            sense.set_pixel(i, j, 255, 255, 0)
        elif distances[i,j] == np.inf:
            sense.set_pixel(i, j, 0, 0, 0)
        else:
            value = 255-int(distances[i,j]*255/maximum)
            if value == 0:
                sense.set_pixel(i, j, 10, 0, 0)
            else:
                sense.set_pixel(i, j, value, 0, 0)
            
sense.flip_h(True)
