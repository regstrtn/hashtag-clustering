import os
import sys
import nltk


def containsin(taglist):
				for tag in taglist:
					if (tag == "IN"):
						return 1
				return 0

def containsdt(taglist):
				for tag in taglist:
								if(tag=='DT'):
												return 1
				return 0

def containsjj(taglist):
				for tag in taglist:
					if (tag == "JJ"):
						return 1
				return 0

def containscc(taglist):
				for tag in taglist:
					if (tag == "JJ"):
						return 1
				return 0

def containsverb(taglist, verbclasslist):
	for tag in taglist:
		if tag in verbclasslist:
			return 1
	return 0

def containsnoun(taglist, nounclasslist):
	for tag in taglist:
		if tag in nounclasslist:
			return 1
	return 0

def numnouns(taglist, nounclasslist):
	counter = 0
	for tag in taglist:
		if tag in nounclasslist:
			counter+=1
	return counter

def numjj(taglist, jjclasslist):
				counter = 0
				for tag in taglist:
								if tag in jjclasslist:
												counter+=1
				return counter

def filter1(taglist):
	verbclasslist = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
	nounclasslist = ['NN', 'NNP', 'NNS', 'NNPS']
	if(len(taglist)>=6): 
					return 0
	else:
		if (containsverb(taglist, verbclasslist) and containsnoun(taglist, nounclasslist)):
			return 1
		elif (numnouns(taglist, nounclasslist)>1):
			return 1
	return 0

def isquerytype(taglist):
	jjclasslist = ['JJ', 'JJS']
	verbclasslist = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
	nounclasslist = ['NN', 'NNS'] 
	if(len(taglist)>=6): 
					#print(taglist, len(taglist))
					return 0
	if(containsdt(nounclasslist) and containsjj(taglist)):
					return 1
	if (filter1(taglist) and len(taglist)<6):
		if (containsjj(taglist) and numnouns(taglist, nounclasslist)>1):
					return 1
		elif(containsin(taglist) and numnouns(taglist, nounclasslist)>1):
					return 1
		elif(containscc(taglist) and numnouns(taglist, nounclasslist)>1):
					return 1
		elif(taglist[-1] == "CD"):
					return 1
		elif(numjj(taglist, jjclasslist)>1):
					return 1
		else: 
			return 0
	else:
			return 0

