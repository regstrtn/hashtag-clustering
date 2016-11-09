import sys
import os


def lenfilter(infilename):
	#fname = sys.argv[1]
	fr = open(infilename,"r")
	outfilename = infilename[:-4]+"_temp"
	fw = open(outfilename, "w")

	for line in fr:
				if(len(line.split())<5):
					fw.write(line)
	os.rename(outfilename, infilename)

if __name__ == '__main__':
	main()