from queue import *

#Node class

class Node:
  #Default constructor
    def __init__(self, value, before):
        self.value = value #value is x,y coordinate
        self.parent = before
    #overloaded constructor for when there is no parent (first node)
    #def __init__(self, value):
    #    self.value = value

#------------------------------------------------------------------------------------
# Neighbors
#------------------------------------------------------------------------------------

#Get Neighbors function
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

        #print(rlist)
        return rlist

#------------------------------------------------------------------------------------
# Expand Node
#------------------------------------------------------------------------------------

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
    #booleans to check if node is already in either the closed or open list
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

#------------------------------------------------------------------------------------
# Input and Output Grid Code
#------------------------------------------------------------------------------------

#provided code for making list
def readGrid(filename):
    grid = []
    with open(filename) as f:
        for l in f.readlines():
            grid.append([int(x) for x in l.split()])    
    f.close()
    return grid

#grid is a 2D array of the board
#start and goal are 2 int tuples like [2,3] or [4,6]
#path is an array of 2 int tuples with the final path (this is NOT an array of nodes, but node values)
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
    #print('Exiting outputGrid')

#------------------------------------------------------------------------------------
# Uninformed Search
#------------------------------------------------------------------------------------
def checklist(nextNode, Visited):
    for loc in Visited:
        if loc.value == nextNode.value:
            return True
    return False



def uninformed(grid, goal, dfs):
      #assumes start is always [0,0] for simplicity
      firstNode = Node([0,0], None) #create parent node
      goalNode = None
      goalFound = False

      Visited = [] #closed list
      q = []
      q.append(firstNode)

      while len(q) != 0 and goalFound is False:
          nextNode = q.pop(-1) if dfs else q.pop(0)
          Visited.append(nextNode)
          for loc in getNeighbors(nextNode.value, grid):
              neighbor = Node(loc, nextNode)
              #check if goal
              if loc[0] == goal[0] and loc[1] == goal[1]:
                    print("Found goal!")
                    goalFound = True
                    goalNode = neighbor
                    break

              #continue if not goal
              if  not checklist(neighbor, Visited):

                 if not checklist(neighbor, q):
                  q.append(neighbor)
                  print(neighbor)
                  #if neigh not in close
                     #check if in open
          print(nextNode.value)









      """
      while len(s) != 0 and goalFound is False:
          nextNode = s.pop(0)
          for loc in getNeighbors(nextNode.value, grid):
              neighbor = Node(loc, nextNode)
              print("check node")
              if loc [0] == goal[0] and loc[1] == goal[1]:
                  print("Found goal!")
                  goalFound = True
                  goalNode = neighbor
                  break

                  if neighbor not in bfsVistied:
                      bfsVisited.append(neighbor)
                      print("push it")
                      s.appdend(neighbor)
      """
      if goalNode is None:
            print("No path to goal found")
            return -1
      
      #backtracking bby
      finalPath = []
      pathCost = 0
      pathNode = goalNode

      finalPath.append(pathNode.value)
      while pathNode != firstNode:
            finalPath.append(pathNode.parent.value)
            pathNode = pathNode.parent
            pathCost += grid[pathNode.value[0]][pathNode.value[1]]

      print("Yas girl u did it!")
      print(finalPath)
      return finalPath
      
      
#------------------------------------------------------------------------------------
# Main
#------------------------------------------------------------------------------------

#code to test existing code
mainGrid = readGrid("grid.txt")
finalPath = uninformed(mainGrid, [4,3],True)
outputGrid(mainGrid, [0,0], [4,3], finalPath)

