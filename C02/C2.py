########################################## 
#   
#  #TuentiChallenge4 (2014).
#  Challenge 2:  F1 - Bird's-eye Circuit
#  https://contest.tuenti.net/Challenges?id=2
#  Isaac Roldan (@saky)
#  
##########################################



test = raw_input("")
c = test[0]
while(c!="#"):
	test = test[1:]+c
	c = test[0]

#create a big matrix, we will start entering data from the center
size = len(test)*2
matrix = [[" " for i in range(int(size))] for j in range(int(size))]
pH = size/2
pV = size/2
index = 0
horizontal = True #0 vertical, 1 horizontal
direccion = True #0 hacia atras, 1 hacia delante
minH = size
minV = size
maxH = 0
maxV = 0
for c in test:

	#save min-max values to crop the matrix later
	if pH < minH:
		minH = pH
	if pV < minV:
		minV = pV
	if pH > maxH:
		maxH = pH
	if pV > maxV:
		maxV = pV

	if not horizontal and c == "-":
		matrix[pV][pH] = "|"
	else:
		matrix[pV][pH] = c

	index += 1
	if index == len(test):
		break
	nextStep = test[index]


	if horizontal:
		if direccion:
			pH += 1
		else:
			pH -= 1
	else:
		if direccion:
			pV += 1
		else:
			pV -= 1

	if nextStep == "\\":
		horizontal = not horizontal
	elif nextStep == "/":
		direccion = not direccion
		horizontal = not horizontal

matrix2 = matrix[minV:maxV+1]
for line in matrix2:
	line2 = line[minH:maxH+1]
	print "".join(line2)


