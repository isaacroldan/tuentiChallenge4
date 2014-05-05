########################################## 
#   
#  #TuentiChallenge4 (2014).
#  Challenge 9: Bendito Caos
#  https://contest.tuenti.net/Challenges?id=9
#  Isaac Roldan (@saky)
#  
##########################################

# This problem is about calculating the max flow from point A to point B in a network
# Algorithm info: http://en.wikipedia.org/wiki/Push%E2%80%93relabel_maximum_flow_algorithm

import sys

def max_flow(C, source, sink):
     n = len(C) # C is the capacity matrix
     F = [[0] * n for _ in xrange(n)]
     # residual capacity from u to v is C[u][v] - F[u][v]
 
     height = [0] * n # height of node
     excess = [0] * n # flow into node minus flow from node
     seen   = [0] * n # neighbours seen since last relabel
     # node "queue"
     nodelist = [i for i in xrange(n) if i != source and i != sink]
 
     def push(u, v):
         send = min(excess[u], C[u][v] - F[u][v])
         F[u][v] += send
         F[v][u] -= send
         excess[u] -= send
         excess[v] += send
 
     def relabel(u):
         # find smallest new height making a push possible,
         # if such a push is possible at all
         min_height = sys.maxint
         for v in xrange(n):
             if C[u][v] - F[u][v] > 0:
                 min_height = min(min_height, height[v])
                 height[u] = min_height + 1
 
     def discharge(u):
         while excess[u] > 0:
             if seen[u] < n: # check next neighbour
                 v = seen[u]
                 if C[u][v] - F[u][v] > 0 and height[u] > height[v]:
                     push(u, v)
                 else:
                     seen[u] += 1
             else: # we have checked all neighbours. must relabel
                 relabel(u)
                 seen[u] = 0
 
     height[source] = n   # longest path from source to sink is less than n long
     excess[source] = sys.maxint # send as much flow as possible to neighbours of source
     for v in xrange(n):
         push(source, v)
 
     p = 0
     while p < len(nodelist):
         u = nodelist[p]
         old_height = height[u]
         discharge(u)
         if height[u] > old_height:
             nodelist.insert(0, nodelist.pop(p)) # move to front of list
             p = 0 # start from front of list
         else:
             p += 1
 
     return sum(F[source])

cases = int(raw_input(""))
for case in range(1,cases+1):
    #g = FlowNetwork()
    name = raw_input("")
    speeds = raw_input("").split(" ")
    normalSpeed = int(speeds[0])*1000
    dirtSpeed = int(speeds[1])*1000
    tracks = raw_input("").split(" ")
    inters = int(tracks[0])
    roads = int(tracks[1])
    matrix = [[0 for col in range(inters+2)] for row in range(inters+2)]
    for road in range(roads):
        path = raw_input("").split(" ")
        #print "PATH",path
        fromVertex = path[0]
        toVertex = path[1]
        roadType = path[2]
        roadLines = int(path[3])
        if fromVertex != "AwesomeVille" and toVertex != name:
            flow = 0
            if roadType == "normal":
                flow = (roadLines * normalSpeed)/5
            else:
                flow = (roadLines * dirtSpeed)/5

            if fromVertex == name:
                fromVertex = inters
            elif fromVertex == "AwesomeVille":
                fromVertex = inters+1
            else:
                fromVertex = int(fromVertex)

            if toVertex == name:
                toVertex = inters
            elif toVertex == "AwesomeVille":
                toVertex = inters+1
            else:
                toVertex = int(toVertex)

            matrix[fromVertex][toVertex] = flow;

    value = max_flow(matrix,inters,inters+1)
    print name + " " + str(value)

