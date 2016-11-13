from __future__ import print_function
import sys
import os
import preprocessing
import lenfilter
import matchregex
import postag1
#import wordsegmentfolder
sys.path.append('/Users/mohammadluqman/Downloads/sem1/nlp/python_code/wordsegmentfolder')
import wordsegment

infilename = sys.argv[1]
cleanfile = infilename[:-4]+"_clean.txt"

'''Remove non ascii characters'''
preprocessing.cleantext(infilename)

'''Match regex'''
matchregex.matchregex(cleanfile)

	
'''Wordsegment file'''
wordsegment.wrapper(cleanfile)
os.rename(cleanfile[:-4]+"_segmented.txt", cleanfile)

'''Get postags'''
postag1.tagpos(cleanfile)

'''Remove specific patterns'''
arglist = cleanfile
bashCommand = "sh removespecificpatterns.sh " + arglist 
os.system(bashCommand)

'''Apply length filter'''
lenfilter.lenfilter(cleanfile)