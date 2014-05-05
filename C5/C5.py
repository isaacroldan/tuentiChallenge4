########################################## 
#   
#  #TuentiChallenge4 (2014).
#  Challenge 5: Tribblemaker
#  https://contest.tuenti.net/Challenges?id=5
#  Isaac Roldan (@saky)
#  
##########################################

import numpy as np

#Really cool method i found here (http://nbviewer.ipython.org/gist/Juanlu001/6260832)
def life_step(X):
    """Game of life step using generator expressions"""
    nbrs_count = sum(np.roll(np.roll(X, i, 0), j, 1)
                     for i in (-1, 0, 1) for j in (-1, 0, 1)
                     if (i != 0 or j != 0))
    return (nbrs_count == 3) | (X & (nbrs_count == 2))

row = 0
X = np.zeros((8, 8), dtype=bool)
allSteps = []
while(1):
	try:
		data = list(raw_input(""))
		for p in range(len(data)):
			if data[p] == "X":
				X[row][p] = True
			else:
				X[row][p] = False
		row += 1

	except EOFError:
		break

def findLoop():
	loop = 100
	origin = 0
	for mat in range(len(allSteps)):
		for k in range(mat,len(allSteps)):
			if mat != k:
				#If the matrix are equal, doing == will result in a matrix with all 64 True
				if sum(sum(allSteps[mat]==allSteps[k])) == 64: 
					if k - mat < loop:
						loop = k - mat
						origin = mat
						print str(origin+1) + " " + str(loop)
						return

for i in xrange(1,100):
	X = life_step(X)
	allSteps.append(X)
findLoop()
