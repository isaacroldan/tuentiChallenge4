########################################## 
#   
#  #TuentiChallenge4 (2014).
#  Challenge 3: The Gambler’s Club - Monkey Island 2
#  https://contest.tuenti.net/Challenges?id=3
#  Isaac Roldan (@saky)
#  
##########################################

import math
cases = int(raw_input(""))
for case in range(1,cases+1):
	try:
		data = list(map(int,raw_input("").split(" ")))
		final = math.sqrt(data[0]**2+data[1]**2) #sqrt(x^2 + y^2)
		rounded = "%.2f" % math.sqrt(data[0]**2+data[1]**2)
		if rounded[-1]=="0":
			print rounded[:-1]
		else:
			print rounded
	except EOFError:
		break
