########################################## 
#   
#  #TuentiChallenge4 (2014).
#  Challenge 1 (https://contest.tuenti.net/Challenges?id=1)
#  Isaac Roldan (@saky)
#  
##########################################

import mmap
cases = int(raw_input(""))
for case in range(1,cases+1):
	try:
		data = raw_input("")
		with open("students", "r+b") as f:
			mm = mmap.mmap(f.fileno(),0)
			found = ""
			for line in f.readlines():
				student = line.split(",",1)
				if student[1] == data+"\n":
					if found == "":
						found = student[0]
					else:
						found = found + "," + student[0]

		if found != "":
			print "Case #" + str(case) + ": " + found
		else:
			print "Case #" + str(case) + ": NONE"

	except EOFError:
		break
