########################################## 
#   
#  #TuentiChallenge4 (2014).
#  Challenge 12: Taxi Driver
#  https://contest.tuenti.net/Challenges?id=12
#  Isaac Roldan (@saky)
#  
##########################################

#This one was a bit tricky!
#Create 4 matrix, each one for values of a direction
#in each one save the minimum distance from to the START until we reach the EXIT.
# i.e. a matrix for the minimum distance to the START when arriving from DOWN to each point
# At the end, compare the numbers in the EXIT position of the 4 matrix and print the lowest

import copy
import sys
import pdb

OBSTACLE = '#'
EXIT = "X"
EXITROW = 0
EXITCOL = 0

class Maze:
    def __init__(self,mazeFileName):
        rowsInMaze = 0
        columnsInMaze = 0
        self.mazelist = []
        rowsInMaze = 0
        deadEndDirections = {}
        for line in mazeFileName:
            rowList = []
            col = 0
            for ch in line:
                rowList.append(ch)
                if ch == 'S':
                    self.startRow = rowsInMaze
                    self.startCol = col
                if ch == 'X':
                    self.endCol = col
                    self.endRow = rowsInMaze
                col = col + 1
            rowsInMaze = rowsInMaze + 1
            self.mazelist.append(rowList)
            columnsInMaze = len(rowList)

        visitedLocationsUp = [[str(sys.maxint) for i in range(int(columnsInMaze))] for j in range(int(rowsInMaze))]
        visitedLocationsDown = [[str(sys.maxint) for i in range(int(columnsInMaze))] for j in range(int(rowsInMaze))]
        visitedLocationsLeft = [[str(sys.maxint) for i in range(int(columnsInMaze))] for j in range(int(rowsInMaze))]
        visitedLocationsRight = [[str(sys.maxint) for i in range(int(columnsInMaze))] for j in range(int(rowsInMaze))]

        self.visitedLocationsUp = visitedLocationsUp
        self.visitedLocationsDown = visitedLocationsDown
        self.visitedLocationsLeft = visitedLocationsLeft
        self.visitedLocationsRight = visitedLocationsRight

        self.rowsInMaze = rowsInMaze
        self.columnsInMaze = columnsInMaze
        self.deadEndDirections = deadEndDirections

    def checkVisited(self,row,col,fromDir):
        key = str(row)+str(col)+fromDir
        if key in self.visitedLocations:
            minimumDistance = self.visitedLocations[key]
            print key + " " + str(minimumDistance)
            return minimumDistance
        else:
            return 0

    def addMinimumDistance(self,row,col,fromDir,distance):
        if fromDir == "DOWN":
            minimumDistance = self.visitedLocationsDown[row][col]
            if int(distance) <= int(minimumDistance):
                self.visitedLocationsDown[row][col] = str(distance)
                return True
            else:
                return False

        elif fromDir == "UP":
            minimumDistance = self.visitedLocationsUp[row][col]
            if int(distance) <= int(minimumDistance):
                self.visitedLocationsUp[row][col] = str(distance)
                return True
            else:
                return False

        elif fromDir == "RIGHT":
            if distance == 1:
                pass
            minimumDistance = self.visitedLocationsRight[row][col]
            if int(distance) <= int(minimumDistance):
                self.visitedLocationsRight[row][col] = str(distance)
                return True
            else:
                return False

        elif fromDir == "LEFT":
            minimumDistance = self.visitedLocationsLeft[row][col]
            if int(distance) <= int(minimumDistance):
                self.visitedLocationsLeft[row][col] = str(distance)
                return True
            else:
                return False
        else:
            return True

    def printMatrix(self,startRow,startColumn,direction,steps):
        print " "
        for line in self.mazelist:
            print " ".join(line)
        print str(startRow) + ":" + str(startColumn) + " > " + direction + " (" + str(steps) + ")"


    def __getitem__(self,idx):
        return self.mazelist[idx]

i = 0

def searchFrom(maze, startRow, startColumn, direction, steps,history):
    #if we are out of borders
    if startRow==-1 or startColumn==-1 or startRow==maze.rowsInMaze or startColumn == maze.columnsInMaze:
        return 0

    #if we hit an obstacle
    if maze[startRow][startColumn] == OBSTACLE :
        return 1000

    #yay! is the exit!
    if maze[startRow][startColumn] == EXIT:
        # print "STEPS!" + str(steps)
        res = maze.addMinimumDistance(startRow,startColumn,direction,steps)
        return 0

    #Add the minimum distance from this direction to the exit
    res = maze.addMinimumDistance(startRow,startColumn,direction,steps)
    if not res:
        return 0

    steps1 = copy.copy(steps)
    steps2 = copy.copy(steps)
    history.append([startRow,startColumn])
    newHistory = (history)
    minimo = sys.maxint
    if direction == "DOWN":
        found = searchFrom(maze, startRow+1, startColumn,direction,steps1+1,newHistory)
        found2 = searchFrom(maze, startRow, startColumn-1,"LEFT",steps2+1,newHistory)
    elif direction == "UP":
        found = searchFrom(maze, startRow-1, startColumn,direction,steps1+1,newHistory)
        found2 = searchFrom(maze, startRow, startColumn+1,"RIGHT",steps2+1,newHistory)
    elif direction == "LEFT":
        found = searchFrom(maze, startRow, startColumn-1,direction,steps1+1,newHistory)
        found2 = searchFrom(maze, startRow-1, startColumn,"UP",steps2+1,newHistory)
    elif direction == "RIGHT":
        found = searchFrom(maze, startRow, startColumn+1,direction,steps1+1,newHistory)
        found2 = searchFrom(maze, startRow+1, startColumn,"DOWN",steps2+1,newHistory)
    else:
        steps3 = copy.copy(steps)
        steps4 = copy.copy(steps)
        found3 = searchFrom(maze, startRow, startColumn-1,"LEFT",steps1+1,newHistory)
        found = searchFrom(maze, startRow, startColumn+1,"RIGHT",steps2+1,newHistory)
        found2 = searchFrom(maze, startRow+1, startColumn,"DOWN",steps3+1,newHistory)
        found4 = searchFrom(maze, startRow-1, startColumn,"UP",steps4+1,newHistory)
    return 0


while(1):
    try:
        cases = int(raw_input(""))
        for p in range(cases):
            size = raw_input("").split(" ")
            M = int(size[0]) #width
            N = int(size[1]) #height
            matrix = []
            for j in range(N):
                line = raw_input("")
                matrix.append(line)

            myMaze = Maze(matrix)
            direction = ""
            steps = 0
            history = []
            m = searchFrom(myMaze, myMaze.startRow, myMaze.startCol, direction, steps,history)
            leftMin = myMaze.visitedLocationsLeft[myMaze.endRow][myMaze.endCol]
            rightMin = myMaze.visitedLocationsRight[myMaze.endRow][myMaze.endCol]
            downMin = myMaze.visitedLocationsDown[myMaze.endRow][myMaze.endCol]
            upMin = myMaze.visitedLocationsUp[myMaze.endRow][myMaze.endCol]

            minimo =  str(min(int(leftMin),int(rightMin),int(downMin),int(upMin)))
            print "Case #" + str(p+1) + ": " + minimo
    except EOFError:
        break


# print m
# for line in myMaze.mazelist:
#     print " ".join(line)
# print "\nDOWN"

# for line in myMaze.visitedLocationsDown:
#     for l in line:
#         if l == str("9223372036854775807"):
#             print "**",
#         else:
#             if len(l)==1:
#                 l = l+" "
#             print l,
#     print ""
# print "\nUP"
# for line in myMaze.visitedLocationsUp:
#     for l in line:
#         if l == str("9223372036854775807"):
#             print "**",
#         else:
#             if len(l)==1:
#                 l = l+" "
#             print l,
#     print ""
# print "\nRIGHT"

# for line in myMaze.visitedLocationsRight:
#     for l in line:
#         if l == str("9223372036854775807"):
#             print "**",
#         else:
#             if len(l)==1:
#                 l = l+" "
#             print l,
#     print ""

# print "\nLEFT"

# for line in myMaze.visitedLocationsLeft:
#     for l in line:
#         if l == str("9223372036854775807"):
#             print "**",
#         else:
#             if len(l)==1:
#                 l = l+" "
#             print l,
#     print ""


