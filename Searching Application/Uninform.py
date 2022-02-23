#Node class
class Node:
  #Default constructor
    def __init__(self, value, before):
        self.value = value
        self.parent = before
    #overloaded constructor for when there is no parent (first node)
    #def __init__(self, value):
    #    self.value = value

#Get Neighbors class
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

def expandNode(oldNode, grid, oList, cList):
  #moves the current node to the closed list
  cList.append(oldNode)
  oList.remove(oldNode)

  #gets list of free locations around node
  tempList = getNeighbors(oldNode.value,grid) 
  listOfNodes = []

  #turns the list of locations generated from getNeighbors into nodes
  for x in tempList:
    tempNode = Node(x, oldNode)
    listOfNodes.append(tempNode)

  #goes through the list of neighbor nodes
  for x in listOfNodes:
    #booleans to check if node is alread in either the closed or open list
    ol = True
    cl = True

    #goes through the open list and makes sure that the node is not there
    for i in range(len(oList)):
      if oList[i].value == x.value:
        ol = False
        break

    #goes through the closed list and makes sure that the node is not there
    for j in range(len(cList)):
      if cList[j].value == x.value:
        cl = False
        break
    
    #if the node was not in either list append it to the open list
    if ol & cl:
      oList.append(x)
  return

#provided code for making list
def readGrid(filename):
    grid = []
    with open(filename) as f:
        for l in f.readlines():
            grid.append([int(x) for x in l.split()])    
    f.close()
    return grid

#code to test existing code
mainGrid = readGrid("./testing.txt")
def readGrid(filename):
    #print('In readGrid')
    grid = []
    with open(filename) as f:
        for l in f.readlines():
            grid.append([int(x) for x in l.split()])

    f.close()
    #print 'Exiting readGrid'
    return grid


# Writes a 2D list of 1s and 0s with spaces in between each character
# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 0 0 1
# 1 1 1 1 1
def outputGrid(grid, start, goal, path):
    #print('In outputGrid')
    filenameStr = 'path.txt'

    # Open filename
    f = open(filenameStr, 'w')

    # Mark the start and goal points
    grid[start[0]][start[1]] = 'S'
    grid[goal[0]][goal[1]] = 'G'

    # Mark intermediate points with *
    for i, p in enumerate(path):
        if i > 0 and i < len(path)-1:
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
    #print('Exiting outputGrid')
firstNode = Node([0,0], None) #create parent node
lastNode = Node(None, [1,1])
#create the open and closed lists that we will need
closedList = []
openList = []
#add parent node to the open list as we have not expanded it yet
openList.append(firstNode)

#expands several nodes to test if the method works
expandNode(firstNode,mainGrid,openList, closedList)
while(len(openList) > 0):
    expandNode(openList[0],mainGrid,openList, closedList)
    
#prints the contents of the open and closed lists
for x in openList:
  print(x.value)
print("-------")
for x in closedList:
  print(x.value)

