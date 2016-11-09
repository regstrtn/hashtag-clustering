from __future__ import print_function
import sys
import os

""" This function removes hashtags which has non-ascci characters """
def ascci(line):
	for char in line:
		if(ord(char)>127):
			return 0
	return 1

""" This function removes hashtags which has symbols in it """
def symbols(line):
	syms = ['.','!','@','#','$','%','^','&','*','(',')','_','+','-','=',',','/',';','\'','<','>','?',':','\"','[',']','{','}','\\','|','~','`']
	for char in line:
		if (char in syms):
			return 0
	return 1

""" Main Function """
def cleantext(infilename):
    flr = open(infilename,"r")
    outfilename = infilename[:-4]+"_clean.txt"
    flw = open(outfilename,"w")
    line = flr.readline()[:-1]
    while line!="":
     if ascci(line)==1 and symbols(line)==1:
      flw.write(line+"\n")
     line = flr.readline()[:-1]	
    flr.close()
    flw.close()

def main():
	infilename = sys.argv[1]
	cleantext(infilename)

if __name__ == "__main__": 
	main()
