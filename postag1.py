import os
import sys
import nltk
from querytype_posrules import isquerytype

def main():
	infilename = sys.argv[1]
	tagpos(infilename)

def tagpos(infilename):
	f = open(infilename, "r+")
	opfile = infilename[0:-4]+"tags.txt"
	fw = open(opfile, "w+")
	tokenized = []
	postags = []
	tagclasses = []
	classlist = []
	flag = 0
	hashtags = []
	nountags = []
	nountagspos = []

	for line in f:
		hashtags.append(line)
		tokenized.append(nltk.word_tokenize(line))
		
	for tags in tokenized:
		postags.append(nltk.pos_tag(tags))

	i = 0

	for item in postags:
		for wordtagtuple in item:
			flag = 0
			classlist.append(wordtagtuple[1])
			#if(isquerytype(classlist)):
			#	flag = 1
		flag = 1
		if(flag ==1 ):
			nountags.append(hashtags[i])
			nountagspos.append(' '.join(classlist))
		classlist = []
		i += 1
		flag = 0


	tagwordsline = []
	i = 0
	for line in nountags:
					j = 0;
					tagwordsline = []
					#for tags, words in  zip(nountagspos[i].split(), nountags[i].split()):
					#	tagwordsline.append(words)
					#	tagwordsline.append(tags)
					#	j = j+1
					fw.write(nountagspos[i].rstrip()+" "+nountags[i].rstrip()+'\n')
					#fw.write(" ".join(tagwordsline))
					#fw.write('\n')
					i+=1
	os.rename(opfile, infilename)

if __name__ == '__main__':
	main()
