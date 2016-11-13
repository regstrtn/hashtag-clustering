from nltk.corpus import wordnet as wn
import os
import pickle
path = "/home/anurag/Downloads/cluster_files"
#path = raw_input("Enter path of the directory containing clusters:\n")
os.chdir(path)
temp = os.listdir(os.getcwd())
head = raw_input("Enter head of the hashtag:\n")
head = head.lower()
clusters = []
flag = False
w1 = head
s1 = wn.synsets(w1)
ss1 = s1[0]

for i in temp:
    clusters.append(i[:-4])
#print clusters
listdir = []
for i in clusters:
	head1 = i
	(x, y) = (head1[1:-1], [])
	f = open(path+"/" + head1 + '.txt', 'rU')
	for line in f:   
	    y.append(line[1:-2])    
	y = ' '.join(y)
	f.close()
	listdir.append((x, y))



     


# define some words
meansim=[]
for i in listdir:
  st=i[1]
  lis=st.split(" ")
  sum=0
  for i in lis:
    #print i
    sq=wn.synsets(i)  
    if(len(sq)>=1):
      ssq = sq[0]
      if(ss1.path_similarity(ssq)!=None):
        sum=sum+float(ss1.path_similarity(ssq))
  mean=sum/len(lis)
  temp = (mean, i)
  meansim.append(temp)  
b = meansim 
b = sorted(b)
print b[-1]
# get synsets



# choose one synset (arbitrary choice here - this is word sense disambiguation)

# Now get the similarity

