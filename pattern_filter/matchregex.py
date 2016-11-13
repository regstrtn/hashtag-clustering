from __future__ import print_function
import os
import re
import sys

def main():
	infilename = sys.argv[1]
	matchregex(infilename)

def matchregex(infilename):		
	infile = infilename
	regexfile = "regexlist.txt"
	outputfile = infilename[0:-4]+"_regex.txt"

	f = open(infile, "r")
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

	regs = set(regexmatchedtags)

	for tag in regs:
					fop.write(tag)

	fop.close()
	f.close()
	fregex.close()
	os.rename(outputfile, infilename)

if __name__=='__main__':
				main()
