########################################## 
#   
#  #TuentiChallenge4 (2014).
#  Challenge 4: Shape shifters
#  https://contest.tuenti.net/Challenges?id=4
#  Isaac Roldan (@saky)
#  
##########################################

import networkx as nx
import numpy as np
import distance

array = []
while(1):
	try:
		array.append(raw_input(""))
	except EOFError:
		break

L = len(array)
A = np.zeros((L,L))

#Create a matrix of distance between states, save only if distance == 1
for i in range(len(array)):
	for j in range(i,len(array)):
		d =	distance.hamming(array[i],array[j])
		if d == 1:
			A[i][j] = 1
			A[j][i] = 1

#Calc dijkstra from start to end state. Easy with nx
G = nx.from_numpy_matrix(A, create_using=nx.DiGraph())
path = nx.dijkstra_path(G, 0, 1)
pathString = ""
for elem in path:
	if pathString == "":
		pathString = array[elem]
	else:
		pathString = pathString + "->" + array[elem]
print pathString

