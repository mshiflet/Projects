import heapq

goal = [4,4]
#Node class
class Node:
  #Default constructor
    #def __init__(self, value, before, step):
        #self.value = value
        #self.parent = before
        
       # if before != None:
          #self.g = before.g + step
       # else:
         # self.g = 0
       # self.h = heuristic(self)
       # self.f = self.g + self.h
    #def __lt__(self, other):
        #return self.f < other.f
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    #overloaded constructor for when there is no parent (first node)


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

  #gets list of free locations around node
  tempList = getNeighbors(oldNode.value,grid) 
  listOfNodes = []

  #turns the list of locations generated from getNeighbors into nodes
  for x in tempList:
    tempNode = Node(x, oldNode, grid[x[0]][x[1]])
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
      #oList.heappush(x)
      heapq.heappush(oList,x)
  return

#provided code for making list
def readGrid(filename):
    grid = []
    with open(filename) as f:
        for l in f.readlines():
            grid.append([int(x) for x in l.split()])    
    f.close()
    return grid

def heuristic(node):
  y = node.value[0]
  x = node.value[1]
    
  return (abs(goal[0] - y) + abs(goal[1] - x))

#code to test existing code
#mainGrid = readGrid("./testing2.txt")
#firstNode = Node([0,0], None, 0) #create parent node
#create the open and closed lists that we will need
#closedList = []
#openList = []
#add parent node to the open list as we have not expanded it yet
#openList.append(firstNode)
#heapq.heappush(openList, firstNode)
#expands several nodes to test if the method works
#expandNode(firstNode,mainGrid,openList, closedList)
#node = heapq.pop(openList)
#expandNode(node,mainGrid,openList, closedList)
#tempNode = openList[2]
#print(openList.index(tempNode))

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


        #found goal
        if currentNode == endNode:
            path =[]
            current = currentNode
            while current is not None:
                path.append(current.postion)
                current = current.parent
            return path[::-1]


        neighbor = []
        for newPosit in getNeighbors:
            #get node loc
            nodePosit = (currentNode.Posit[0] + newPosit[0] + currentNode[1] + newPosit[1])
            # check range
            if nodePosit[0] > (len(grid) - 1) or nodePosit[0] < 0 or nodePosit[1] > (len(grid[len(grid)-1])-1) or nodePosit[1] < 0:
                continue
            if grid[nodePosit[0]][nodePosit[1]] !=0:
                continue

                #create new node
                newNode = Node(currentNode, nodePosit)

                neighbor.append(newNode)
                #if neighbor is in closed list
        for neighbor in neighbors:
            for closedNeighbor in closedList:
                if neighbor == closedNeighbor:
                    continue

            neighbor.g = currentNode.g + 1
            neighbor.h = ((neighbor.postition[0] - endNode.postition[0]) ** 2 ) + (neighbor.position[1] - endNode.position[1] ** 2)
            neighbor.f = neighbor.g + neighbor.h

            for openNode in openList:
                if neighbor == openNode and neighbor.g > openNode.g:
                    continue

                openList.append(neighbor)


def main():

    grid = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (7, 6)

    path = astar(grid, start, end)
    print(path)


if __name__ == '__main__':
    main()
