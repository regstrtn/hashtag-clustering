from __future__ import print_function
import os
import re

filetoread = "million_tags.txt"
regexfile = "regexlist.txt"
outputfile = "regexmatchedqueries2.txt"

f = open(filetoread, "r")
fregex = open(regexfile, "r")
fop = open(outputfile, "w")
regexmatchedtags = []

for line in fregex:
	f.seek(0)
	#print(line)
	for hashtag in f:
			m = re.match(line, hashtag)
			if m:
				#print(hashtag)
				regexmatchedtags.append(hashtag)

for tag in regexmatchedtags:
				fop.write(tag)
