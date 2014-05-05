#!/usr/bin/env python
# -*- coding: utf-8 -*-

########################################## 
#   
#  #TuentiChallenge4 (2014).
#  Challenge 17: The Failsystem
#  https://contest.tuenti.net/Challenges?id=17
#  Isaac Roldan (@saky)
#  
##########################################

# I Really liked this challenge, you have a FAT32 disk image and have to find
# some missing files (or find out if they are corrupt)

# I didn't implement directory searching and finding files starting from the root to all the tree
# I directly search file the by the name and start getting data from there
# Yes, this could cause problems if two files have the same name, i know

import mmap
import binascii
import md5

cluster_size = 4096
first_cluster = 6278656 #(5fce00)
FATstart = 1049600
EOF = "f8ffff0f"
ERROR = "00000000"

def getNextCluster(mm,cluster,index):
	clusterInFat = index*4+FATstart
	#print "current cluster index pos: " + str(clusterInFat)
	next_pos = mm.seek(clusterInFat)
	data = mm.read(4)
	checkError = binascii.hexlify(data)
	if checkError==EOF:
		return EOF, 0
	if checkError==ERROR:
		return ERROR, 0
	#print "data: " + checkError
	next_index = int(binascii.hexlify(data[2]+data[1]+data[0]), 16)
	#print "next index: "+str(next_index)
	hex_string = binascii.hexlify(data[2]+data[1]+data[0])+"000" #(+000 to multiply for 4096)
	#print "hex string: "+str(hex_string)
	next_cluster_pos = int(hex_string, 16) + first_cluster
	return next_cluster_pos, next_index

#Recursive method to read all the data from a file starting in cluster.
def readFileAtCluster(mm,cluster,index,history):
	if cluster in history:
		return "CORRUPT"
	if cluster == EOF:
		return
	elif cluster == ERROR:
		return "CORRUPT"
	if cluster > 5368709184:
		return "CORRUPT"
	mm.seek(cluster)
	data = mm.read(4096)
	nextpos, next_index = getNextCluster(mm,cluster,index)
	history.append(cluster)
	newData = readFileAtCluster(mm,nextpos,next_index,history)
	if newData:
		return data + newData
	else:
		return data

def md5ofdata(res):
	if "CORRUPT" in res:
		return "CORRUPT"
	else:
		m = md5.new()
		m.update(res)
		return m.hexdigest()



cases = int(raw_input(""))
with open("TUENTIDISK.BIN", "r+b") as f:
	mm = mmap.mmap(f.fileno(),0)
	for case in range(cases):		
		path = raw_input("").split("/")
		fileName = path[-1].split(".")
		name = fileName[0]
		ext = ""
		if len(fileName)>1:
			ext = fileName[1]
		nameSize = len(name)
		extSize = len(ext)
		name = name + " "*(8-nameSize)
		ext = ext + " "*(3-extSize)
		finalName = name+ext

		pos = mm.find(finalName)

		if pos>0:
			mm.seek(pos)
			data = mm.read(32) #read file metadata
			cluster_index = int(binascii.hexlify(data[20]+data[27]+data[26]), 16)
			hex_string = binascii.hexlify(data[20]+data[27]+data[26])+"000" #(+000 to multiply for 4096)
			fileSize = int(binascii.hexlify(data[31]+data[30]+data[29]+data[28]), 16)

			first_file_cluster = int(hex_string, 16) + first_cluster
			res = readFileAtCluster(mm,first_file_cluster,cluster_index,[])
			f2 = open("./aaa/"+finalName+".txt","w")
			f2.write(res[:fileSize])
			f2.close()
			if "CORRUPT" in res:
				print "CORRUPT"
			else:
				res = res[:fileSize]
				print md5ofdata(res)
		else:
			print "CORRUPT"
				
	

