import nqueens
import random

B = nqueens.Board(4)
B.rand()
#first decayRate = .95

def schedulingFunction(Temp, decayRate):
  return Temp * decayRate

def simulatedAnnealing(initBoard, decayRate, T_Threshold): 
  Temp = 100 #what is this supposed to be
  current = initBoard
  #heurCost = nqueens.numAttackingQueens(current)
  current.h = nqueens.numAttackingQueens(current)
  
  while(Temp > T_Threshold and current.h > 0):
    Temp = schedulingFunction(Temp, decayRate)
    successorList = nqueens.getSuccessorStates(current)


    for x in successorList:
      x.h = nqueens.numAttackingQueens(x)
    
    #selects truly random next node
    current = successorList[random.randint(0,len(successorList)-1)]


  return current

print(simulatedAnnealing(B, .95, 50))
B.printBoard()