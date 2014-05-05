########################################## 
#   
#  #TuentiChallenge4 (2014).
#  Challenge 11: Pheasant
#  https://contest.tuenti.net/Challenges?id=11
#  Isaac Roldan (@saky)
#  
##########################################

#we have AES keys with the 3 last characters missing, bruteForce them all the keys :D
#This algorithm is not very efficient, but it works!

from Crypto.Cipher import AES
from operator import itemgetter
import itertools
import rbtree

dataDecripted={}
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def bruteForce(userKey,encriptedData,timestamp,userID):
	if userID in dataDecripted:
		return dataDecripted[userID]
	for l in letters:
		for l2 in letters:
			for l3 in letters:
				key = userKey + l + l2 + l3
				decobj = AES.new(key, AES.MODE_ECB)
				plaintext = decobj.decrypt(encriptedData)
				if plaintext.find(timestamp) > 0:
					dataDecripted[userID] = plaintext
					return plaintext

i = 0
import re
while(1):
	try:
		feed = raw_input("").split("; ")
		maxFeeds = int(feed[0])
		totalData = []
		r = rbtree.rbtree() #ordered dictinary
		for u in range(1,len(feed)):
			userID = feed[u].split(",")[0]
			userKey = feed[u].split(",")[1]
			folderFeed = "feeds/encrypted/"+userID[-2:]+"/"+userID+".feed"
			folderTime = "feeds/last_times/"+userID[-2:]+"/"+userID+".timestamp"
			f1= open(folderFeed)
			f2 = open(folderTime)
			feedEncriptedData = f1.read()
			lastTimeStamp = f2.read()
			data = bruteForce(userKey,feedEncriptedData,lastTimeStamp,userID)
			f1.close()
			f2.close()
			data2 = [s.strip().split(' ') for s in data.splitlines()][:-1]
			for event in data2:
				if len(event)>2:
					r[int(event[1])] = event[2]
			totalData.append(data2)
		keys = r.keys()[-maxFeeds:][::-1]
		stringFinal = ""
		for key in keys:
			if stringFinal == "":
				stringFinal = r[key]
			else:
				stringFinal = stringFinal + " " + r[key]
		print stringFinal
		#totalData = list(itertools.chain(*totalData))
		i+=1
	except EOFError:
		break
