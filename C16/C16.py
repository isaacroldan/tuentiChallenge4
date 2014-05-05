########################################## 
#   
#  #TuentiChallenge4 (2014).
#  Challenge 16: ÑAPA
#  https://contest.tuenti.net/Challenges?id=16
#  Isaac Roldan (@saky)
#  
##########################################

#this one was hard for me to make it efficient
#At the end for 20.000 points it needs 1.4s (not bad!) 
# and for 2.000.000 about 100m (not that good)

# Uses mmap to access the file
# Multiprocessing, up to 4 cores to make it 4 times faster

import mmap
import math
from operator import itemgetter
from multiprocessing import Pool
numbers = raw_input("").split(",")
start = int(numbers[0])
length = int(numbers[1])
bytes = 27

def getcercanosFromX(p,lines):
	newArray = lines
	for j in range(0,len(lines),50):
		if len(lines[j])<3:
				continue
		p2 = lines[j]
		if abs(int(p2[0])-int(p[0]))>int(p[2])+500:
			newArray = lines[:j]
			#if a point is further than radius+500, then all the next points can't collisionate,
			#break and save the subarray until this point	
			break
	return newArray


#Same than in previous method, but dividing in two:
#First order the points in Y, then filter from the original comparing point
# to upper points and to lower points, the merge the array to get the "cercanos"
def filterY(p,lines):
	lines.append(p)
	sortedList = sorted(lines, key=itemgetter(1))
	index = sortedList.index(p)
	newList = []
	listA = sortedList[index+1:]
	for i in range(index+1,len(sortedList),2):
		p2 = sortedList[i]
		if abs(int(p2[1])-int(p[1]))>=int(p[2])+500:
			listA = sortedList[index+1:i]
			break
	listB = sortedList[:index]
	for j in range(index-1,-1,-2):
		p2 = sortedList[j]
		if abs(int(p2[1])-int(p[1]))>=int(p[2])+500:
			listB = sortedList[j+1:index]
			break
	newList = listA+listB
	return newList



def process(i):
	if len(linesX[i])<3:
		return 0
	p = linesX[i]	

	#From the ordered list, make a first filter, filter in X the next 5000 points
	#No need to compare more, it's very improbable the a point has collisions with 5000 points
	#This helps speeding up a lot
	cercanosFromX = getcercanosFromX(p,linesX[i+1:i+5000])
	if not cercanosFromX:
		return 0
	#After filtering in X, filter in Y
	cercanosFromY = filterY(p,cercanosFromX)

	#After filtering, apply the distance formula to detect colisions
	#This formula (sqrt(x^2+y^2)) is only applied to a few points after filtering
	colisions = 0
	for j in range(len(cercanosFromY)):
		p2 = cercanosFromY[j]
		if math.sqrt((int(p[0])-int(p2[0]))**2+(int(p[1])-int(p2[1]))**2)<(int(p[2])+int(p2[2])):
			colisions += 1
	return colisions



with open("points", "r+b") as f:
	mm = mmap.mmap(f.fileno(),0)
	colisions = 0
	mm.seek(bytes*(start-1))
	lines = mm.read(bytes*length).split("\n")
	lines = [i.split('\t') for i in lines]
	#order in the X coordinate, so we compare only with the nearest points
	linesX = sorted(lines, key=itemgetter(0))

	if linesX[0] == [""]:
		del linesX[0]

	pool = Pool(processes=4) #Multiprocesing, yesssss
	res = pool.map(process, range(len(linesX)))
	res = sum(res)
	print str(res)


		