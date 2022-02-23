from queue import *


class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def getNeighbors(loc, grid):
        #takes locations given and stores them each seperatly
        y = loc[0]
        x = loc[1]
        #defines the coordinates of the nodes around the original
        up = y-1
        down = y+1
        left = x-1
        right = x+1
        #create list that will be returned
        rlist = []
        templist = []

        #checks to make sure that the modified grid values are valid indexs
        if down < len(grid):
          templist.append([down, x])
        if up > -1:
          templist.append([up, x])
        if left > -1:
          templist.append([y, left])
        if right < len(grid[0]):
          templist.append([y, right])

        #for each valid index append the coordinates to the return list


        for x in templist:
          if(grid[x[0]][x[1]]) != 0:
            rlist.append([x[0],x[1]])

        print(rlist)
        return rlist

def readGrid(filename):
    grid = []
    with open(filename) as f:
        for l in f.readlines():
            grid.append([int(x) for x in l.split()])
    f.close()
    return grid

def outputGrid(grid, start, goal, path): #start and goal are 2 int tuples, path is array of xy tuples
    #print('In outputGrid')
    filenameStr = 'path1.txt'
    print(path)
    # Open filename
    f = open(filenameStr, 'w')

    # Mark the start and goal points
    grid[start[0]][start[1]] = 'S'
    grid[goal[0]][goal[1]] = 'G'

    # Mark intermediate points with *
    for i, p in enumerate(path):
        if i > 0 and i < len(path)-1: #checks to see if in grid
            grid[p[0]][p[1]] = '*'

    # Write the grid to a file
    for r, row in enumerate(grid):
        for c, col in enumerate(row):

            # Don't add a ' ' at the end of a line
            if c < len(row)-1:
                f.write(str(col)+' ')
            else:
                f.write(str(col))

        # Don't add a '\n' after the last line
        if r < len(grid)-1:
            f.write("\n")

    # Close file
    f.close()


def astar(grid, start , end):
    startNode = Node(None,start)
    startNode.g = startNode.h = startNode.f = 0
    endNode = Node(None,end)
    endNode.g = endNode.h = endNode.f = 0

    #initilize the list
    openList = []
    closedList = []

    #add start node
    openList.append(startNode)

    #loop list till end is found
    while len(openList) > 0:

        #get current node
        currentNode = openList[0]
        currentIndex = 0
        for index, item in enumerate(openList):
            if item.f < currentNode.f:
                currentNode = item
                currentIndex = index

        #pop off current open list and add to closed list
        openList.pop(currentIndex)
        closedList.append(currentNode)
        print("current: %s" % currentNode.position)

        #found goal
        if currentNode.position == end:
            print("Found goal")
            path =[]
            current = currentNode
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]


        neighbors = []
        for newPosit in getNeighbors(currentNode.position, grid):
            #get node loc
            #nodePosit = (currentNode.position[0] + newPosit[0] + currentNode.position + newPosit[1])
            # check range
            if newPosit[0] > (len(grid) - 1) or newPosit[0] < 0 or newPosit[1] > (len(grid[len(grid)-1])-1) or newPosit[1] < 0:
                continue
            if grid[newPosit[0]][newPosit[1]] ==0:
                continue

                #create new node
            newNode = Node(currentNode, newPosit)

            neighbors.append(newNode)
                #if neighbor is in closed list
        for neighbor in neighbors:
            for closedNeighbor in closedList:
                if neighbor == closedNeighbor:
                    continue

            neighbor.g = currentNode.g + neighbor.position[0] - neighbor.position[1] # get the number from the grid at neighbor position grid[]
            neighbor.h = ((neighbor.position[0] - end[0]) ** 2 ) + (neighbor.position[1] - end[1] ** 2)
            neighbor.f = neighbor.g + neighbor.h
            print(len(openList))
            print("neighbor: %s" % neighbor.position)
            toAdd = True
            for openNode in openList:
                print("openNode.pos: %s" % openNode.position)
                if neighbor.position == openNode.position and neighbor.g > openNode.g:
                    toAdd = False
                print("Adding to openlist")
            if toAdd:
                openList.append(neighbor)
        print(len(openList))
    finalPath = []
    pathCost = 0
    pathNode = currentNode

    finalPath.append(pathNode.position)
    print("pathnode.position: %s" % pathNode.position)
    print("start: %s" % start)
    while pathNode.position != start:
        finalPath.append(pathNode.parent.position)
        pathNode = pathNode.parent
        pathCost += grid[pathNode.position[0]][pathNode.position[1]]

    print("Yas girl u did it!")
    print(finalPath)
    return finalPath



mainGrid = readGrid("grid.txt")
finalPath = astar(mainGrid, [0,0], [4,3])
outputGrid(mainGrid, [0,0], [4,3], finalPath)
print(finalPath)
